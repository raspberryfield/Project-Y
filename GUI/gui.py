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
import sqlite3
import json
import subprocess


class Entity:
    def __init__(self, checkbox, checkbox_var, name):
        self.checkbox = checkbox
        self.checkbox_var = checkbox_var
        self.lbl_name = name
        # How to acces values:
        # Lable : entity.lbl_name.get['text'] 

class AppPage(tk.Tk):
    def __init__(self):
        super().__init__()

        #self.geometry("540x100") - How to set fixed window size.
        self.title('Project-Y')
        # self.resizable(1, 1) # uncomment to allow user to resize the window.

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure([1,2], weight=8)

        # Styles
        self.style = ttk.Style(self)
        self.style.configure("Header.TLabel", foreground="white", background="black")
        self.style.configure("Info.TLabel", foreground="black", background="white")

        # l1 = ttk.Label(text="Test", style="BW.TLabel")
        #self.style.configure('Heading.TLabel', font=('Helvetica', 12))
        #heading = ttk.Label(self, text='Member Login', style='Heading.TLabel')

        # Structure
        self.row_start_header = 0
        self.row_start_entities = 1
        self.row_start_info_section = 2
        
        self.create_header_section()

        

        self.entities = []
        self.create_entities()

        self.create_info_section()
        self.create_button_section()
        
        

    def create_header_section(self):
        # Todo: create a Entity object of this and loop the grid.
        # checkbox
        self.chbox_header_var = tk.StringVar()
        self.checkbox = ttk.Checkbutton(self, variable=self.chbox_header_var)
        self.checkbox.grid(column=0, row=self.row_start_header)
        # name
        self.lbl_header_name = ttk.Label(self, text="NAME", style="Header.TLabel")
        self.lbl_header_name.grid(column=1, row=self.row_start_header, sticky="nesw")
        # status
        self.lbl_header_info = ttk.Label(self, text="STATUS", style="Header.TLabel")
        self.lbl_header_info.grid(column=2, row=self.row_start_header, sticky="nesw")

    def create_entities(self):
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
            checbox_var = tk.StringVar()
            checkbox = ttk.Checkbutton(self, variable=checbox_var)
            lbl_name = ttk.Label(text=obj["name"])
            entity = Entity(checkbox, checbox_var, lbl_name)
            self.entities.append(entity)
        # self.entities - grid
        for index, entity in enumerate(self.entities):
            entity.checkbox.grid(column=0, row=index+self.row_start_entities)
            entity.lbl_name.grid(column=1, row=index+self.row_start_entities, sticky="nesw")
            self.row_start_info_section += 1 # Dynamically set the row that the info label can start on.

        # test
        for entry in self.entities:
            print(entry.lbl_name["text"])
        
    def create_info_section(self):
        # Frame
        self.frame_info_section = ttk.Frame(self)
        self.frame_info_section.grid(column=0, row=4, columnspan=3)
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
                test = (subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE).stdout.read())
                print(test)
                self.text_info_section['state'] = 'normal'
                self.text_info_section.insert(tk.END, test)
  


if __name__ == "__main__":
    app = AppPage()
    app.mainloop()

# https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
