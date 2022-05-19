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
import time

BLACK = "#141414" #"#262626"
WHITE = "#ffffff"
DARK_GREEN = "#047b80"
VERY_DARK_GREEN = "#014145"
GREY = "#6b6a6a"
DARK_GREY = "#545454"
VERY_DARK_GREY = "#363535"


class AppPage(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurations
        # window
        self.title('PROJECT-Y')
        self.eval('tk::PlaceWindow . center') #centers window on start.
        self.resizable(tk.FALSE, tk.FALSE)
        # configure the grid
        self.columnconfigure(0, weight=1) # CHECKBOX
        self.columnconfigure([1,2], weight=8) # TEXT | STATUS
        self.columnconfigure([3,4], weight=4) # BUILT | INFO

        # Styles
        # Style config
        self.style = ttk.Style(self)
        self.style.theme_use('default')
        # header styles
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
        self.style.configure("Entity.TButton", foreground=WHITE, background=VERY_DARK_GREY)
        self.style.map('Entity.TButton', background=[('active', DARK_GREY)],
            indicatorcolor=[('selected', DARK_GREEN)])
        # info textbox styles
        self.style.configure("Info.TFrame", background=BLACK)
        # scrollbar style
        self.style.configure("Vertical.TScrollbar", background=VERY_DARK_GREY, troughcolor=VERY_DARK_GREY, arrowcolor=WHITE, borderwidth=0.5)
        self.style.map("Vertical.TScrollbar", background=[('active', DARK_GREY)], troughcolor=[('active', VERY_DARK_GREY)], arrowcolor=[('active', WHITE)],
            indicatorcolor=[('selected', GREY)])
        # button/cmd pane style
        self.style.configure("Cmd.TFrame", background=BLACK)
        self.style.configure("Cmd.TButton", foreground=WHITE, background=VERY_DARK_GREEN)
        self.style.map('Cmd.TButton', background=[('active', DARK_GREEN)],
            indicatorcolor=[('selected', DARK_GREEN)])

        #print("test")
        #self.config(cursor="watch")
        ##time.sleep(4)
        #print("end test")

        
        # Structure
        # Render order
        self.row_start_header = 0
        self.row_start_entities = 1
        self.row_start_info_section = 2 # this will be incremented by the entity loop.
        # Header
        self.create_header_section()
        # Entities
        self.entities = []
        self.create_entity_section()
        # Info
        self.create_info_section()
        # Buttons
        self.create_button_section()
        
    # Header
    def create_header_section(self):
        # Checkbox
        self.frame_checkbox_header = ttk.Frame(self, style="Header.TFrame")
        self.frame_checkbox_header.grid(column=0, row=self.row_start_header, sticky="NSEW")
        self.checkbox_header_var = tk.StringVar()
        self.checkbox_header = ttk.Checkbutton(self.frame_checkbox_header, variable=self.checkbox_header_var,
                                        style="Header.TCheckbutton", command=self.toogle_checkboxes)
        self.checkbox_header.pack()
        # Name
        self.label_header_name = ttk.Label(self, text="NAME", style="Header.TLabel")
        self.label_header_name.grid(column=1, row=self.row_start_header, sticky="nesw")
        # Status
        self.label_header_info = ttk.Label(self, text=" STATUS", style="Header.TLabel")
        self.label_header_info.grid(column=2, row=self.row_start_header, sticky="nesw")
        # Built
        self.label_header_info = ttk.Label(self, text=" BUILT", style="Header.TLabel")
        self.label_header_info.grid(column=3, row=self.row_start_header, sticky="nesw")
        # Info
        self.label_header_info = ttk.Label(self, text=" ", style="Header.TLabel")
        self.label_header_info.grid(column=4, row=self.row_start_header, sticky="nesw")
    # checkbox function
    def toogle_checkboxes(self):
        if self.checkbox_header_var.get() == "1":
            for entity in self.entities:
                entity.checkbox_var.set("1")
        else:
            for entity in self.entities:
                entity.checkbox_var.set("0")

    # Entities
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
            # Store objects in list
            entity = self.Entity(obj)
            self.entities.append(entity)
        # self.entities - grid/display
        for index, entity in enumerate(self.entities):
            entity.frame_checkbox.grid(column=0, row=index+self.row_start_entities, sticky="NSEW")
            entity.label_name.grid(column=1, row=index+self.row_start_entities, sticky="NSEW")
            entity.label_status.grid(column=2, row=index+self.row_start_entities, sticky="NSEW")
            entity.label_built.grid(column=3, row=index+self.row_start_entities, sticky="NSEW")
            entity.frame_button.grid(column=4, row=index+self.row_start_entities, sticky="NSEW")
            # Dynamically set the row that the info label can start on.
            self.row_start_info_section += 1

    # Info box
    def create_info_section(self):
        # Frame
        self.frame_info_section = ttk.Frame(self, style="Info.TFrame")
        self.frame_info_section.grid(column=0, row=self.row_start_info_section, columnspan=5)
        # Text
        self.text_info_section = tk.Text(self.frame_info_section, height=8, state="disable", background=BLACK, foreground=WHITE,
                                        highlightthickness=1, highlightbackground=VERY_DARK_GREY)
        self.text_info_section.pack(side='left')
        # Scrollbar
        self.text_info_scrollbar = ttk.Scrollbar(self.frame_info_section, style="Vertical.TScrollbar", orient='vertical', command=self.text_info_section.yview)
        self.text_info_scrollbar.pack(side='right', fill='both')
        #  communicate back to the scrollbar
        self.text_info_section['yscrollcommand'] = self.text_info_scrollbar.set
    # Helper functions to give feedback to the user:
    # display
    def display_text(self, message):
        self.text_info_section['state'] = 'normal'
        self.text_info_section.insert(tk.END, message + " \n")
        self.text_info_section['state'] = 'disable'
        self.text_info_section.see("end") # autoscroll
    def display_raw_text(self, message):
        self.text_info_section['state'] = 'normal'
        self.text_info_section.insert(tk.END, message)
        self.text_info_section['state'] = 'disable'
        self.text_info_section.see("end") # autoscroll
    # cursor watch/wait
    def cursor_watch(self, watch):
        if watch:
            self.config(cursor="watch")
            self.text_info_section.config(cursor="watch")
        else:
            self.config(cursor="")
            self.text_info_section.config(cursor="xterm")
        self.update() # Force update so the cursor change don't wait for another event.

    # Button Section
    def create_button_section(self):
        # Frame
        self.frame_button_section = ttk.Frame(self, style="Cmd.TFrame")
        self.frame_button_section.grid(column=0, row=self.row_start_info_section+1, columnspan=5, sticky="ew")
        # Buttons
        # build
        self.button_build = ttk.Button(self.frame_button_section, style="Cmd.TButton", text="BUILD", command=self.build_cmd)
        self.button_build.pack(side='right', padx=(0,4), pady=4)
        # status
        self.button_status = ttk.Button(self.frame_button_section, style="Cmd.TButton", text="STATUS", command=self.status_cmd)
        self.button_status.pack(side='right', padx=(0,4), pady=(5,2))
    # Commands
    # build
    def build_cmd(self):
        self.cursor_watch(True)
        for entity in self.entities:
            if entity.checkbox_var.get() == "1":
                self.display_text("Building: " + entity.entity['name'])
                stdout_build = (subprocess.Popen(entity.entity['buildCmd'], shell=True, stdout=subprocess.PIPE).stdout.read())
                self.display_raw_text(stdout_build)
        self.status_cmd()
        self.cursor_watch(False)
    # status
    def status_cmd(self):
        self.cursor_watch(True)
        stdout_image_ls = str(subprocess.Popen('docker image ls', shell=True, stdout=subprocess.PIPE).stdout.read()) # list docker images.
        stdout_process_status = str(subprocess.Popen('docker ps', shell=True, stdout=subprocess.PIPE).stdout.read()) # list docker running processes.
        print(str(stdout_process_status))
        checked_entities = 0
        for entity in self.entities:
            if entity.checkbox_var.get() == "1":
                checked_entities += 1
                # build status
                self.display_text("Checking build status for: " + entity.entity['name'])
                built = True # Not guilty until otherwise proven.
                for name in entity.entity['imageName']:
                    if stdout_image_ls.rfind(name) != -1:
                        self.display_text(" * " + name + " - OK")
                        continue
                    else:
                        self.display_text(" * " + name + " - NOT OK")
                        built = False
                if built:
                    entity.label_built.config(text = " YES")
                else:
                    entity.label_built.config(text = " NO")
                # running status
                if built:
                    self.display_text("Checking run status for: " + entity.entity['name'])
                    running = True # Not guilty until otherwise proven.
                    for name in entity.entity['imageName']:
                        if stdout_process_status.rfind(name) != -1:
                            self.display_text(" * " + name + " - RUNNING")
                            continue
                        else:
                            self.display_text(" * " + name + " - STOPPED")
                            running = False
                    if running:
                        entity.label_status.config(text = " RUNNING")
                    else:
                        entity.label_status.config(text = " STOPPED")
        # if nothing checked
        if checked_entities == 0:
            self.display_text("Check the checkboxes for the entities you want to display the status for.")
        self.cursor_watch(False)
    # #


                #self.text_info_section['state'] = 'normal'
                #self.text_info_section.insert(tk.END, entity.lbl_name['text'] + " \n")
                #self.text_info_section['state'] = 'disable'
                #self.text_info_section.see("end") # autoscroll
                ## test
                #print("---")
                #print(entity.build_cmd)
                #test = (subprocess.Popen(entity.build_cmd, shell=True, stdout=subprocess.PIPE).stdout.read())
                #print(test)
                #self.text_info_section['state'] = 'normal'
                #self.text_info_section.insert(tk.END, test)
    

    class Entity():
        def __init__(self, docker_resource):
            # object values
            self.entity = docker_resource
            # checkbox
            self.frame_checkbox = ttk.Frame(style="Entity.TFrame")
            self.checkbox_var = tk.StringVar()
            self.checkbox = ttk.Checkbutton(self.frame_checkbox, variable=self.checkbox_var, style="Entity.TCheckbutton")
            self.checkbox.pack()
            # labels
            self.label_name = ttk.Label(text=self.entity["name"], style="Entity.TLabel")
            self.label_status = ttk.Label(text=" UNKNOWN", style="Entity.TLabel")
            self.label_built = ttk.Label(text=" ?", style="Entity.TLabel")
            # button
            self.frame_button = ttk.Frame(style="Entity.TFrame")
            self.button = ttk.Button(self.frame_button, text="INFO", style="Entity.TButton", 
                                command=self.show_info_message
                                )
            self.button.pack(side='right')
        # Methods
        def show_info_message(self):
            title = self.entity['name']
            message = self.entity['description'] + "\n\n"
            message = message + "Access: \n"
            for dictionary in self.entity['access']:
                for key,value in dictionary.items():
                    message = message + "\u2022 " + key + " - " + value + "\n"
            message = message + "\n" + "Additional Information: " + "\n"
            for item in self.entity['additionalInformation']:
                if item == "None":
                    message = message + "None"
                    break
                else:
                    message = message + "\u2022 " + item + "\n"
            showinfo(title=title,message=message) # global tk function.

if __name__ == "__main__":
    app = AppPage()
    app.mainloop()

# Executing shell commands: https://stackoverflow.com/questions/89228/how-do-i-execute-a-program-or-call-a-system-command
# Tkinter tutorial, very good: https://www.pythontutorial.net/tkinter/tkinter-hello-world/

# https://docs.python.org/3/library/tk.html
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/checkbutton.html
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Checkbutton.html
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-map.html

# http://www.tcl.tk/scripting/index.tml

# THIS! : https://profjahier.github.io/html/NSI/tkinter/doc_tk_allegee/tutorial/eventloop.html

# docker run -p 80:80 --name y-nginx --rm -d y-nginx
# docker stop y-nginx

# TODO: network