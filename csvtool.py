from struct import pack
from tkinter import *
from tkinter import filedialog as fd
import tkinter
from tkinter.ttk import *

csvfiles = []

root = Tk()
root.geometry('200x100')
label = Label(root, text="CSV Selector")
root.title('CSV Comparison Tool')


def file_selection():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    csvfiles.append(filename)

button1 = Button(root, text = 'Select your first CSV', command = file_selection)
button2 = Button(root, text = 'Select your second CSV', command = file_selection)
button3 = Button(root, text = 'Process Files / Close Window', command = root.destroy)

button1.pack(side=tkinter.TOP)
button2.pack(side=tkinter.TOP)
button3.pack(side=tkinter.BOTTOM)  

root.mainloop()

print(csvfiles)