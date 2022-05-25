# How To Add Scrollbar To The Frame In Tkinter - Python
# https://www.youtube.com/watch?v=VmlgrrXAqb4

from tkinter import *
from tkinter import ttk

from click import command

win = Tk()

# LabelFrames
wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)

#Canvas
my_canvas = Canvas(wrapper1)
my_canvas.pack(side=LEFT, fill="both")

yscrollbar = ttk.Scrollbar(wrapper1, orient="vertical", command=my_canvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")

my_canvas.configure(yscrollcommand=yscrollbar.set)

my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

# Canvas Frame
my_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=my_frame, anchor="nw")


wrapper1.pack(fill="both", expand="yes", padx=10, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)

for i in range(50):
    Button(my_frame, text="My Button - "+str(i)).pack()

win.geometry("500x500")
win.resizable(False, False)
win.title("MyScroller")
win.mainloop()
