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

class AppPage(tk.Tk):
    def __init__(self):
        super().__init__()

        #self.geometry("540x100")
        self.title('Project-Y')
        self.resizable(1, 1)

        # configure the grid
        #self.columnconfigure(0, weight=1)
        #self.columnconfigure([1,2], weight=2)

        self.style = ttk.Style()
        self.style.configure("BW.TLabel", foreground="black", background="white")

        # l1 = ttk.Label(text="Test", style="BW.TLabel")

        self.label_list = []

        self.create_info_label()
        self.create_entries()

    def create_info_label(self):
        # checkbox
        agreement = tk.StringVar()
        self.checkbox = ttk.Checkbutton(self, variable=agreement)
        self.checkbox.grid(column=0, row=1, sticky="nesw")
        # name
        self.lbl_name = ttk.Label(self, text="NAME", style="BW.TLabel")
        self.lbl_name.grid(column=1, row=1, sticky="nesw")

    def create_entries(self):
        for i in range(2,4):
            lbl_name = ttk.Label(text="NAME"+str(i), style="BW.TLabel")
            self.label_list.append(lbl_name)
        for index, value in enumerate(self.label_list):
            value.grid(column=1, row=index+2, sticky="nesw")

if __name__ == "__main__":
    app = AppPage()
    app.mainloop()

