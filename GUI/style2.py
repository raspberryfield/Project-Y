import tkinter as tk
from tkinter import ttk

# https://www.pythontutorial.net/tkinter/ttk-elements/
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        style = ttk.Style(self)

        layout = style.layout('TCheckbutton')
        # print(layout)

        element_option = style.element_options('Checkbutton.focus')
        print(element_option)

        print(style.lookup('Checkbutton.focus', 'focusthickness'))


if __name__ == "__main__":
    app = App()
    app.mainloop()