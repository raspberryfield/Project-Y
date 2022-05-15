#import tkinter as tk
#
#window = tk.Tk()
#
#frame1 = tk.Frame(master=window, height=100, bg="red")
#frame1.pack(fill=tk.X)
#
#label = tk.Label(master=frame1, text="hello world!")
#label.pack()
#
#
#frame2 = tk.Frame(master=window, height=50, bg="yellow")
#frame2.pack(fill=tk.X)
##
##frame3 = tk.Frame(master=window, height=25, bg="blue")
##frame3.pack(fill=tk.X)
#
#window.mainloop()

# https://stackoverflow.com/questions/50422735/tkinter-resize-frame-and-contents-with-main-window
# https://stackoverflow.com/questions/6129899/python-multiple-frames-with-grid-manager
# https://medium.datadriveninvestor.com/how-to-create-structure-a-complex-tkinter-application-2022-26e4a9907a6d

# https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
# https://pythonprogramming.net/change-show-new-frame-tkinter/
# https://www.pythontutorial.net/tkinter/tkinter-grid/

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
import json
import subprocess

BLACK = "#000000"
WHITE = "#ffffff"
DARK_GREEN = "#047b80"
VERY_DARK_GREEN = "#014145"
DARK_GREY = "#545454"

class Entity:
    def __init__(self, frame_checkbox, checkbox_var, label_name, label_status, label_built):
        self.frame_checkbox = frame_checkbox
        self.checkbox_var = checkbox_var
        self.label_name = label_name
        self.label_status = label_status
        self.label_built = label_built
        #self.build_cmd = build_cmd
        # How to acces values:
        # Lable : entity.lbl_name.get['text'] 

class AppPage(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurations
        # window
        self.title('Project-Y')
        self.resizable(tk.FALSE, tk.FALSE)
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure([1,2], weight=8)
        self.columnconfigure([3,4], weight=4)

        # Styles
        # header styles
        self.style = ttk.Style(self)
        self.style.configure("Header.TFrame", background=VERY_DARK_GREEN)
        self.style.configure("Header.TCheckbutton", background=VERY_DARK_GREEN, indicatorcolor=WHITE)
        self.style.map('Header.TCheckbutton', background=[('active', DARK_GREEN)],
            indicatorcolor=[('selected', DARK_GREEN)])
        self.style.configure("Header.TLabel", foreground=WHITE, background=VERY_DARK_GREEN)
        # entity styles
        self.style.configure("Entity.TFrame", background=BLACK)
        self.style.configure("Entity.TCheckbutton", background=BLACK, indicatorcolor=WHITE)
        self.style.map('Entity.TCheckbutton', background=[('active', DARK_GREY)],
            indicatorcolor=[('selected', DARK_GREEN)])
        self.style.configure("Entity.TLabel", foreground=WHITE, background=BLACK)

        # Structure
        # Render order
        self.row_start_header = 0
        self.row_start_entities = 1
        self.row_start_info_section = 2
        # Header
        self.create_header_section()
        # Entities
        self.entities = []
        self.create_entity_section()

        #self.create_info_section()
        #self.create_button_section()
        
        

    def create_header_section(self):
        # Checkbox
        self.frame_checkbox_header = ttk.Frame(self, style="Header.TFrame")
        self.frame_checkbox_header.grid(column=0, row=self.row_start_header, sticky="NSEW")
        self.checkbox_header_var = tk.StringVar()
        self.checkbox_header = ttk.Checkbutton(self.frame_checkbox_header, variable=self.checkbox_header_var, style="Header.TCheckbutton")
        self.checkbox_header.pack()
        # Name
        self.lbl_header_name = ttk.Label(self, text="NAME", style="Header.TLabel")
        self.lbl_header_name.grid(column=1, row=self.row_start_header, sticky="nesw")
        # Status
        self.lbl_header_info = ttk.Label(self, text=" STATUS", style="Header.TLabel")
        self.lbl_header_info.grid(column=2, row=self.row_start_header, sticky="nesw")
        # Built
        self.lbl_header_info = ttk.Label(self, text=" BUILT", style="Header.TLabel")
        self.lbl_header_info.grid(column=3, row=self.row_start_header, sticky="nesw")
        # Info
        #self.lbl_header_info = ttk.Label(self, text="INFO", style="Header.TLabel")
        #self.lbl_header_info.grid(column=4, row=self.row_start_header, sticky="nesw")

        self.button_info = ttk.Button(self,
                                    text='Show an information message',
                                    command=lambda: showinfo(
                                        title='Information',
                                        message='This is an \n information message.'))
        self.button_info.grid(column=4, row=self.row_start_header, sticky="NESW")


    def create_entity_section(self):
        # DB - sqlite
        con = sqlite3.connect('projecty.sqlitedb')
        cur = con.cursor()
        db_entities = []
        for row in cur.execute("SELECT id, data FROM entities ORDER BY id ASC"):
            db_entities.append(json.loads(row[1]))
        cur.close()
        con.close()
        # self.entities - store
        for obj in db_entities:
            # Checkbox
            frame_checkbox = ttk.Frame(self, style="Entity.TFrame")
            checkbox_var = tk.StringVar()
            checkbox = ttk.Checkbutton(frame_checkbox, variable=checkbox_var, style="Entity.TCheckbutton")
            checkbox.pack()
            # Label
            label_name = ttk.Label(text=obj["name"], style="Entity.TLabel")
            label_status = ttk.Label(text=" UNKNOWN", style="Entity.TLabel")
            label_built = ttk.Label(text=" ?", style="Entity.TLabel")
            # Store
            entity = Entity(frame_checkbox, checkbox_var, label_name, label_status, label_built)
            self.entities.append(entity)

            #checbox_var = tk.StringVar()
            #checkbox = ttk.Checkbutton(self, variable=checbox_var)
            
            #lbl_name = ttk.Label(text=obj["name"])
            #build_cmd = obj["buildCmd"]
            #entity = Entity(frame_checkbox, checkbox_var, lbl_name, build_cmd)
            #self.entities.append(entity)
        # self.entities - grid/display
        for index, entity in enumerate(self.entities):
            entity.frame_checkbox.grid(column=0, row=index+self.row_start_entities, sticky="NSEW")
            entity.label_name.grid(column=1, row=index+self.row_start_entities, sticky="NSEW")
            entity.label_status.grid(column=2, row=index+self.row_start_entities, sticky="NSEW")
            entity.label_built.grid(column=3, row=index+self.row_start_entities, sticky="NSEW")
            # Dynamically set the row that the info label can start on.
            self.row_start_info_section += 1

        # test
        #for entry in self.entities:
            #print(entry.lbl_name["text"])
        
    def create_info_section(self):
        # Frame
        self.frame_info_section = ttk.Frame(self)
        self.frame_info_section.grid(column=0, row=4, columnspan=4)
        # Text
        self.text_info_section = tk.Text(self.frame_info_section, height=4, state="disable")
        self.text_info_section.pack(side='left')
        # Scrollbar
        self.text_info_scrollbar = ttk.Scrollbar(self.frame_info_section, orient='vertical', command=self.text_info_section.yview)
        self.text_info_scrollbar.pack(side='right', fill='both')
        #  communicate back to the scrollbar
        self.text_info_section['yscrollcommand'] = self.text_info_scrollbar.set

    def create_button_section(self):
        # Frame
        self.frame_button_section = ttk.Frame(self)
        self.frame_button_section.grid(column=0, row=5, columnspan=3, sticky="e")
        # RUN - button
        self.button_run = ttk.Button(self.frame_button_section, text="RUN", command=self.run_cmd)
        self.button_run.pack(side='right', padx=4, pady=4)
    
    def run_cmd(self):
        for index, entity in enumerate(self.entities):
            if entity.checkbox_var.get() == "1":
                self.text_info_section['state'] = 'normal'
                self.text_info_section.insert(tk.END, entity.lbl_name['text'] + " \n")
                self.text_info_section['state'] = 'disable'
                self.text_info_section.see("end") # autoscroll
                # test
                print("---")
                print(entity.build_cmd)
                test = (subprocess.Popen(entity.build_cmd, shell=True, stdout=subprocess.PIPE).stdout.read())
                print(test)
                self.text_info_section['state'] = 'normal'
                self.text_info_section.insert(tk.END, test)
  


if __name__ == "__main__":
    app = AppPage()
    app.mainloop()

# Executing shell commands: https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
# Tkinter tutorial, very good: https://www.pythontutorial.net/tkinter/tkinter-hello-world/

# https://docs.python.org/3/library/tk.html
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/checkbutton.html
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Checkbutton.html
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-map.html

