from struct import pack
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.geometry('300x300')
label = Label(root, text="CSV Selector")
root.title('CSV Comparison Tool')


def OpenWindow(WindowName):

    newWindow = Toplevel(root)

    newWindow.title(WindowName)

    newWindow.geometry('200x200')

    Label(newWindow,text = 'Select the CSV File you need').pack()

    button = Button(root, text = 'Open FIle', command = )



button = Button(root, text = 'Select your first CSV', command = lambda: OpenWindow('Select the 1st CSV File'))
button = Button(root, text = 'Select your second CSV', command = lambda: OpenWindow('Select the 2nd CSV File'))

button.pack(pady=10)



mainloop()