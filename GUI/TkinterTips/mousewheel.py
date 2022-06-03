# How To Add Scrollbar To The Frame In Tkinter - Python - https://www.youtube.com/watch?v=VmlgrrXAqb4

# Mousewheel tips:
# https://stackoverflow.com/questions/6863921/python-tkinter-canvas-xview-units
# https://stackoverflow.com/questions/17355902/tkinter-binding-mousewheel-to-scrollbar

from tkinter import *
from tkinter import ttk

from click import command

win = Tk()

# Widgets
# LabelFrames
wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)
# Canvas
my_canvas = Canvas(wrapper1)
my_canvas.pack(side=LEFT, fill="both")
# Scrollbar
yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=my_canvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")
my_canvas.configure(yscrollcommand=yscrollbar.set)
# bind scrollbar
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))
# Canvas Frame
my_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=my_frame, anchor="nw")

# Drawings
# Start Drawing things
wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

def on_mousewheel(event):
    print("scroll")
    direction = 0
    if event.num == 5 or event.delta == -120:
     direction = 2
    if event.num == 4 or event.delta == 120:
     direction = -2
    my_canvas.yview_scroll(direction, UNITS)

for i in range(50):
     my_button = Button(my_frame, text="My Button - "+str(i))
     my_button.bind('<Button-4>', on_mousewheel, add='+') # Linux scroll up
     my_button.bind('<Button-5>', on_mousewheel, add='+')
     my_button.pack()


wrapper1.bind('<Button-4>', on_mousewheel, add='+') # Linux scroll up
wrapper1.bind('<Button-5>', on_mousewheel, add='+')
my_canvas.bind('<Button-4>', on_mousewheel, add='+') # Linux scroll up
my_canvas.bind('<Button-5>', on_mousewheel, add='+')


win.geometry("500x500")
win.resizable(False, False)
win.title("MyScroller")
win.mainloop()


