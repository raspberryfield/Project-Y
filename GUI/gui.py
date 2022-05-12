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

import tkinter as tk

window = tk.Tk()

# weight=1 makes alement grow if there are space left.
window.rowconfigure([0, 1], weight=1, minsize=75)
window.columnconfigure([0, 1], weight=1, minsize=75)


frame1 = tk.Frame(master=window, bg="red")
frame1.grid(row=0, column=0, columnspan=2, sticky="nesw")
#sticky=tk.W+tk.E+tk.N+tk.S

#label = tk.Label(master=frame1, text="Hello World!")
#label.pack()


#for i in range(3):
#    window.columnconfigure(i, weight=1, minsize=75)
#    window.rowconfigure(i, weight=1, minsize=50)
#
#    for j in range(0, 3):
#        frame = tk.Frame(
#            master=window,
#            relief=tk.RAISED,
#            borderwidth=1
#        )
#        frame.grid(row=i, column=j, padx=5, pady=5)
#        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#        label.pack(padx=5, pady=5)

window.mainloop()

