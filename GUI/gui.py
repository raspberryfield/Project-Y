# Articles/videos that I read/watch to learn tkinter:
# https://www.youtube.com/playlist?list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk (good video series)
# https://pythonprogramming.net/change-show-new-frame-tkinter/ (new window)
# https://www.pythontutorial.net/tkinter/tkinter-hello-world/ (best beginner to intermideate resource)
# https://docs.python.org/3/library/tk.html (python official? don't cover evereything thou)
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-map.html (very good semi-official docs.)
# http://www.tcl.tk/scripting/index.tml (tcl/tk documentation, underlying libraries of tkinter.)
# https://profjahier.github.io/html/NSI/tkinter/doc_tk_allegee/tutorial/eventloop.html (explains the event loop!)
# https://dafarry.github.io/tkinterbook/ (didn't use it much, but could be good resource.)

from email.header import Header
import tkinter as tk
from tkinter import BOTH, ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import sqlite3
import json
import subprocess
import time
from turtle import width

BLACK = "#141414" #"#262626"
WHITE = "#ffffff"
DARK_GREEN = "#047b80"
VERY_DARK_GREEN = "#014145"
GREY = "#6b6a6a"
DARK_GREY = "#545454"
VERY_DARK_GREY = "#363535"

CANVAS_HEIGHT = 120 # 90-three entities; 120-four entities;
INFO_SECTION_HEIGHT = 12 # 8-original
INFO_SECTION_WIDTH = 90 # 90-good number


class AppPage(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurations
        # window
        self.title('PROJECT-Y')
        self.eval('tk::PlaceWindow . center') #centers window on start.
        self.resizable(tk.FALSE, tk.FALSE)
        
        # configure the grid
        self.columnconfigure(0, weight=1) #Everything is treated as it exists in one column. Except for the selection section that has its own grid.

        # Styles
        # Style config
        self.style = ttk.Style(self)
        self.style.theme_use('default')
        # filter section style
        self.style.configure("Filter.TFrame", background=BLACK)
        self.style.configure("Filter.TButton", foreground=WHITE, background=VERY_DARK_GREEN)
        self.style.map('Filter.TButton', background=[('active', DARK_GREEN)], indicatorcolor=[('selected', DARK_GREEN)])
        self.style.configure("Filter.TMenubutton", foreground=WHITE, background=VERY_DARK_GREY, indicatorcolor=WHITE)
        self.style.map('Filter.TMenubutton', background=[('active', DARK_GREY)],
            indicatorcolor=[('selected', DARK_GREEN)]) #Note, the style of the pop up menu is in the filter section.
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

        # Structure
        # render order
        self.row_start_filter_section = 0
        self.row_start_header = 1
        self.row_start_selection = 2
        self.row_start_info_section = 3
        self.row_start_action_section = 4
        # Sections
        # filter section
        self.create_filter_section()
        # header
        self.create_header_section()
        # selection
        self.entities = []
        self.create_selection_section()
        # info
        self.create_info_section()
        # action / buttons
        self.create_action_section()

        # Draw (place, pack or grid)
        # Info:
        '''
        The text widget is using the default width. Which works fine as a width for this application. However, the widget is behaving in kind of
        canonical way. It pushes the main window to fit itself. Some frames have problem to dynamically adapt to this behaviour. Since it behaves 
        like a 'master' let's start with it, So we get the full width window immediately.
        '''
        self.frame_info_section.grid(row=self.row_start_info_section, column=0)
        self.update() # Force update so info box is drawn so we get the correct window width.
        # Selection:
        '''
        The selection section is a frame with a scrollable canvas and its own grid. It's hard to make it fit the width dynamically.
        The solution is to pass in the root windows width after the largest widget (info box) is drawn.
        '''
        self.frame_entity_section.grid(row=self.row_start_selection, column=0, sticky="NSEW")
        self.draw_entities(self.winfo_width())
        # Header:
        '''
        The header section is not aware about the grid in the canvas. The align function looks at the coordinates in the canvas grid and
        uses thoose values to place the header labels so they are aligned. Therefore this must be draw after the selection section.
        '''
        self.frame_header.grid(row=self.row_start_header, column=0, sticky="NSEW")
        self.draw_aligned_header_section()
        # Action/Buttons:
        '''
        Everything must be drawn before the action section, because the commands here uses all objects in the application.
        '''
        self.frame_button_section.grid(column=0, row=self.row_start_action_section, columnspan=5, sticky="ew")
        # Filter section
        '''
        Filter section is similar to the button section and can be drawn last.
        '''
        self.frame_filter_section.grid(column=0, row=self.row_start_filter_section, columnspan=5, sticky="ew")
        # END Draw

    def create_header_section(self):
        # Frame
        self.frame_header = ttk.Frame(self, height=25, style="Header.TFrame")
        #self.frame_header.grid(column=0, row=self.row_start_header, columnspan=5, sticky="NSEW")
        # Checkbox
        self.frame_checkbox_header = ttk.Frame(self, style="Header.TFrame")
        #self.frame_checkbox_header.grid(column=0, row=self.row_start_header, sticky="NSEW")
        self.checkbox_header_var = tk.StringVar()
        self.checkbox_header = ttk.Checkbutton(self.frame_checkbox_header, variable=self.checkbox_header_var,
                                        style="Header.TCheckbutton", command=self.toogle_checkboxes)
        self.checkbox_header.pack()
        # Name
        self.label_header_name = ttk.Label(self, text="NAME", style="Header.TLabel")
        # Status
        self.label_header_status = ttk.Label(self, text="STATUS", style="Header.TLabel")
        # Built
        self.label_header_built = ttk.Label(self, text="BUILT", style="Header.TLabel")
    def draw_aligned_header_section(self):
        # grid_bbox(): https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/grid-methods.html
        self.update() # Force update so we can get the cells real values.
        self.header_top_padding = 38 # with no filter section it was 3.
        self.checkbox_left_padding = 0.08 * INFO_SECTION_WIDTH # Something is causing that grid_bbox don't give accurate value related to root window for first cell?
        self.last_row = len(self.entities)-1 # last entry in the list would have been pushed in representativ position for all.
        position_checkbox = self.frame_canvas.grid_bbox(0, self.last_row) # returns tuple -> (x, y, width, height)
        self.frame_checkbox_header.place(x=position_checkbox[0]+self.checkbox_left_padding, y=self.header_top_padding ) # (x, y)
        position_label_name = self.frame_canvas.grid_bbox(1, self.last_row)
        self.label_header_name.place(x=position_label_name[0], y=self.header_top_padding )
        position_label_status = self.frame_canvas.grid_bbox(2, self.last_row)
        self.label_header_status.place(x=position_label_status[0], y=self.header_top_padding )
        position_label_built = self.frame_canvas.grid_bbox(3, self.last_row)
        self.label_header_built.place(x=position_label_built[0], y=self.header_top_padding )
    # header checkbox function
    def toogle_checkboxes(self):
        if self.checkbox_header_var.get() == "1":
            for entity in self.entities:
                entity.checkbox_var.set("1")
        else:
            for entity in self.entities:
                entity.checkbox_var.set("0")

    def create_selection_section(self):
        # Frame
        self.frame_entity_section = ttk.Frame(self, style="Test.TFrame") # TODO: change style here?
        # Canvas (only text and canvas widgets are scrollable) https://www.youtube.com/watch?v=VmlgrrXAqb4
        self.canvas_entities = tk.Canvas(self.frame_entity_section, height=CANVAS_HEIGHT, bg=BLACK, highlightbackground=VERY_DARK_GREY)
        self.canvas_entities.pack(side='left', fill=BOTH, expand=True)
        # Scrollbar
        self.scrollbar_entities = ttk.Scrollbar(self.frame_entity_section, style="Vertical.TScrollbar", orient='vertical', command=self.canvas_entities.yview)
        self.scrollbar_entities.pack(side='right', fill='both')
        self.canvas_entities['yscrollcommand'] = self.scrollbar_entities.set
        # Bind
        self.canvas_entities.bind('<Configure>', lambda event: self.canvas_entities.configure(scrollregion=self.canvas_entities.bbox("all")))
        # Create a frame to contain the entities
        self.frame_canvas = ttk.Frame(self.canvas_entities, style="Test2.TFrame")
        #self.canvas_entities.create_window((0,0), window=self.frame_canvas, anchor="nw")
        # Configuration of the grid
        self.frame_canvas.columnconfigure(0, weight=1) # CHECKBOX
        self.frame_canvas.columnconfigure([1,2], weight=8) # TEXT | STATUS
        self.frame_canvas.columnconfigure([3,4], weight=4) # BUILT | INFO
        # Populate list with entities
        # db-sqlite - get entities
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
            entity = self.Entity(obj, self.frame_canvas)
            self.entities.append(entity)   
    def draw_entities(self, window_width):
        self.canvas_entities.create_window((0,0), window=self.frame_canvas, anchor="nw", width=window_width-20) # -20, give room for scrollbar.
        # self.entities - grid/display
        for index, entity in enumerate(self.entities):
            # bindings
            entity.label_name.bind('<Button-4>', self.on_mousewheel) # Linux mousewheel scroll up
            entity.label_name.bind('<Button-5>', self.on_mousewheel) # Linux mousewheel scroll down
            entity.label_status.bind('<Button-4>', self.on_mousewheel)
            entity.label_status.bind('<Button-5>', self.on_mousewheel)
            entity.label_built.bind('<Button-4>', self.on_mousewheel)
            entity.label_built.bind('<Button-5>', self.on_mousewheel)
            entity.frame_button.bind('<Button-4>', self.on_mousewheel)
            entity.frame_button.bind('<Button-5>', self.on_mousewheel)
            # widgets
            entity.frame_checkbox.grid(column=0, row=index, sticky="NSEW")
            entity.label_name.grid(column=1, row=index, sticky="NSEW")
            entity.label_status.grid(column=2, row=index, sticky="NSEW")
            entity.label_built.grid(column=3, row=index, sticky="NSEW")
            entity.frame_button.grid(column=4, row=index, sticky="NSEW")
    def on_mousewheel(self,event):
        direction = 0
        if event.num == 5 or event.delta == -120:
            direction = 2
        if event.num == 4 or event.delta == 120:
            direction = -2
        self.canvas_entities.yview_scroll(direction, tk.UNITS)

    def draw_entities_test(self):
        for index, entity in enumerate(self.entities):
            print("drawing")
            # widgets
            entity.frame_checkbox.grid(column=0, row=index, sticky="NSEW")
            entity.label_name.grid(column=1, row=index, sticky="NSEW")
            entity.label_status.grid(column=2, row=index, sticky="NSEW")
            entity.label_built.grid(column=3, row=index, sticky="NSEW")
            entity.frame_button.grid(column=4, row=index, sticky="NSEW")
            self.update()
    

    # Info box
    def create_info_section(self):
        # Frame
        self.frame_info_section = ttk.Frame(self, style="Info.TFrame")
        #self.frame_info_section.grid(column=0, row=self.row_start_info_section, columnspan=5)
        # Text
        self.text_info_section = tk.Text(self.frame_info_section, height=INFO_SECTION_HEIGHT, width=INFO_SECTION_WIDTH, state="disable", background=BLACK, foreground=WHITE,
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
    def clear_text(self):
        self.text_info_section['state'] = 'normal'
        self.text_info_section.delete(1.0, tk.END)
        self.text_info_section['state'] = 'disable'
    def stream_text_sdtout(self, cmd):
        # https://stackoverflow.com/questions/18421757/live-output-from-subprocess-command
        process = (subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        for c in iter(lambda: process.stdout.read(True), b""):
            self.display_raw_text(c)
            self.update()
        for c in iter(lambda: process.stderr.read(True), b""):
            self.display_raw_text(c)
            self.update()
    # cursor watch/wait
    def cursor_watch(self, watch):
        if watch:
            self.config(cursor="watch")
            self.text_info_section.config(cursor="watch")
        else:
            self.config(cursor="")
            self.text_info_section.config(cursor="xterm")
        self.update() # Force update so the cursor change don't wait for another event.

    # Action/Button Section
    def create_action_section(self):
        # Frame
        self.frame_button_section = ttk.Frame(self, style="Cmd.TFrame")
        #self.frame_button_section.grid(column=0, row=self.row_start_info_section+1, columnspan=5, sticky="ew")
        # Buttons
        # run
        self.button_run = ttk.Button(self.frame_button_section, style="Cmd.TButton", text="RUN", command=self.run_cmd)
        self.button_run.pack(side='right', padx=(0,4), pady=4)
        # stop
        self.button_stop = ttk.Button(self.frame_button_section, style="Cmd.TButton", text="STOP", command=self.stop_cmd)
        self.button_stop.pack(side='right', padx=(0,4), pady=4)
        # build
        self.button_build = ttk.Button(self.frame_button_section, style="Cmd.TButton", text="BUILD", command=self.build_cmd)
        self.button_build.pack(side='right', padx=(0,4), pady=4)
        # status
        self.button_status = ttk.Button(self.frame_button_section, style="Cmd.TButton", text="STATUS", command=self.status_cmd)
        self.button_status.pack(side='right', padx=(0,4), pady=(5,2))
        # status
        self.button_clear = ttk.Button(self.frame_button_section, style="Cmd.TButton", text="CLEAR", command=self.clear_cmd)
        self.button_clear.pack(side='right', padx=(0,4), pady=(5,2))
    # Commands
    # run
    def run_cmd(self):
        self.cursor_watch(True)
        for entity in self.entities:
            if entity.checkbox_var.get() == "1":
                self.display_text("Running: " + entity.entity['name'])
                self.stream_text_sdtout(entity.entity['runCmd'])
                self.status_running_check(entity)
        self.cursor_watch(False)
    # stop
    def stop_cmd(self):
        self.cursor_watch(True)
        for entity in self.entities:
            if entity.checkbox_var.get() == "1":
                self.display_text("Stopping: " + entity.entity['name'])
                self.stream_text_sdtout(entity.entity['stopCmd'])
                self.status_running_check(entity)
        self.cursor_watch(False)
    # build
    def build_cmd(self):
        self.cursor_watch(True)
        for entity in self.entities:
            if entity.checkbox_var.get() == "1":
                self.display_text("Building: " + entity.entity['name'])
                self.stream_text_sdtout(entity.entity['buildCmd'])
        self.status_cmd()
        self.cursor_watch(False) 
    # status
    def status_cmd(self):
        self.cursor_watch(True)
        checked_entities = 0
        for entity in self.entities:
            if entity.checkbox_var.get() == "1":
                checked_entities += 1
                # build status
                is_built = self.status_build_check(entity)
                # running status
                if is_built:
                    self.status_running_check(entity)
        # if nothing checked
        if checked_entities == 0:
            self.display_text("Check the checkboxes for the entities you want to display the status for.")
        self.draw_aligned_header_section() # Align header so it aligns with the cells when they change position after new values are drawn.
        self.cursor_watch(False)   
    # status - build check
    def status_build_check(self, entity):
        process = (subprocess.Popen('docker image ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        stdout = str(process.stdout.read()) # search string
        self.display_text("Checking build status for: " + entity.entity['name'])
        built = True # Not guilty until otherwise proven.
        for name in entity.entity['imageName']:
            if stdout.rfind(name) != -1:
                self.display_text(" * " + name + " - OK")
                continue
            else:
                self.display_text(" * " + name + " - NOT OK")
                built = False  
        if entity.entity['buildNeeded'] == False:
            self.display_text(" NOTE! Build not needed for this image/compose file.")
            entity.label_built.config(text = "N/A")
            return True
        elif built:
            entity.label_built.config(text = "YES")
            return True
        else:
            entity.label_built.config(text = "NO")
            return False
    # status - running check
    def status_running_check(self, entity):
        stdout_process_status = str(subprocess.Popen('docker ps', shell=True, stdout=subprocess.PIPE).stdout.read()) # list docker running processes.
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
            entity.label_status.config(text = "RUNNING")
            return True
        else:
            entity.label_status.config(text = "STOPPED")
            return False
    # clear
    def clear_cmd(self):
        # clear checkboxes
        self.checkbox_header_var.set("0")
        for entity in self.entities:
            entity.checkbox_var.set("0")
        # clear info box
        self.clear_text()

    # Filter Section
    def create_filter_section(self):
        # Frame
        self.frame_filter_section = ttk.Frame(self, style="Filter.TFrame")
        # Buttons
        # filter
        self.button_filter = ttk.Button(self.frame_filter_section, style="Filter.TButton", text="FILTER", command=self.filter_cmd)
        self.button_filter.pack(side='right', padx=(0,18), pady=4)
        # DROPDOWN MENU
        ## options
        self.filter_tags = ('ALL', 'DATA WAREHOUSE', 'DATA LAKEHOUSE')
        ## variable to hold the option
        self.filter_tags_var = tk.StringVar(self)
        self.filter_tags_menu = ttk.OptionMenu(self.frame_filter_section, self.filter_tags_var, self.filter_tags[0], 
            *self.filter_tags, direction='below', style="Filter.TMenubutton")
        self.filter_tags_menu["menu"].configure(fg="white", bg="black", activeforeground="white", activebackground=VERY_DARK_GREY)
        self.filter_tags_menu.pack(side='right', padx=(0,4), pady=4)


    # filter
    def filter_cmd(self):
        self.cursor_watch(True)
        print("filter button pressed.")
        for entity in self.entities:
            print (entity.entity['name'])
            if entity.entity['name'] == 'AIRBYTE':
                print("removing")
                # widgets
                entity.frame_checkbox.grid_remove()
                entity.label_name.grid_remove()
                entity.label_status.grid_remove()
                entity.label_built.grid_remove()
                entity.frame_button.grid_remove()
            self.update()
        #self.canvas_entities.delete("all")
        #self.draw_entities_test()
        self.cursor_watch(False)




    class Entity():
        def __init__(self, docker_object, widget_context):
            # object values
            self.entity = docker_object
            # widget context
            self.widget = widget_context
            # checkbox
            self.frame_checkbox = ttk.Frame(self.widget, style="Entity.TFrame")
            self.checkbox_var = tk.StringVar()
            self.checkbox = ttk.Checkbutton(self.frame_checkbox, variable=self.checkbox_var, style="Entity.TCheckbutton")
            self.checkbox.pack()
            # labels
            self.label_name = ttk.Label(self.widget, text=self.entity["name"], style="Entity.TLabel")
            self.label_status = ttk.Label(self.widget, text="UNKNOWN", style="Entity.TLabel")
            self.label_built = ttk.Label(self.widget, text="?", style="Entity.TLabel")
            # button
            self.frame_button = ttk.Frame(self.widget, style="Entity.TFrame")
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
