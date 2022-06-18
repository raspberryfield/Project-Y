import tkinter as tk
import tkinter.ttk as ttk

# https://stackoverflow.com/questions/45389166/how-to-know-all-style-options-of-a-ttk-widget
def stylename_elements_options(stylename):
    '''Function to expose the options of every element associated to a widget
       stylename.'''
    try:
        # Get widget elements
        style = ttk.Style()
        layout = str(style.layout(stylename))
        print('Stylename = {}'.format(stylename))
        print('Layout    = {}'.format(layout))
        elements=[]
        for n, x in enumerate(layout):
            if x=='(':
                element=""
                for y in layout[n+2:]:
                    if y != ',':
                        element=element+str(y)
                    else:
                        elements.append(element[:-1])
                        break
        print('\nElement(s) = {}\n'.format(elements))

        # Get options of widget elements
        for element in elements:
            print('{0:30} options: {1}'.format(
                element, style.element_options(element)))

    except tk.TclError:
        print('_tkinter.TclError: "{0}" in function'
              'widget_elements_options({0}) is not a regonised stylename.'
              .format(stylename))

# https://www.pythontutorial.net/tkinter/ttk-style/
#stylename_elements_options('my.Vertical.TScrollbar')
stylename_elements_options('TCheckbutton')
stylename_elements_options('TFrame')
stylename_elements_options('TButton')
stylename_elements_options('Vertical.TScrollbar')
stylename_elements_options('TMenubutton') # this covers optionmenu also https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Menubutton.html.
print("----- ----- -----")
# stylename_elements_options('TCanvas') see: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
# for styling optionmenu, see: https://stackoverflow.com/questions/40793670/how-to-edit-ttk-style-for-ttk-optionmenu
# The style name for an OptionMenu is not TOptionMenu. For any widget the style name can get obtained using widget.winfo_class().
# To change the background of the drop down menu: my_optionmenu["menu"].configure(bg="black") If you run: print(my_optionmenu["menu"].keys()) you get all of the options you can change for the OptionMenu widge

'''
    A ttk widget is made up of elements. The layout determines how elements assembled the widget.
    Use the Style.layout() method to retrieve the layout of a widget class.
    Use the Style.element_options() method to get the element options of an element.
    Use the Style.lookup() method to get the attributes of an element option.
'''

# https://stackoverflow.com/questions/28375591/changing-the-appearance-of-a-scrollbar-in-tkinter-using-ttk-styles
