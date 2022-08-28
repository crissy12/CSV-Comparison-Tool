from email import message
from struct import pack
from tkinter import *
from tkinter import filedialog as fd
import tkinter
from tkinter.ttk import *
import csv
import re

csvfiles = []

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

root = Tk()
root.geometry('200x100')
label = Label(root, text="CSV Selector")
root.title('CSV Comparison Tool')
fusemail_emails = []
active_emails = []

def file_selection():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    return filename

def fusemail_action():
    filename = file_selection()
    get_info (fusemail_emails,filename)
   

def active_action():
    filename = file_selection()
    get_info (active_emails,filename)
    


def get_info(list_to_use,filename):
    with open (str(filename)) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            list_to_use.extend(list(filter(lambda x: re.match(regex,x),row)))
    return (list_to_use)

def process_files():
    print('\n\n******************************************************************************\n')
    print('******************************************************************************\nItems to remove from Fusemail\n')
    for fusemail_item in fusemail_emails:
        if fusemail_item not in active_emails:
            print (fusemail_item)
    

first_csv_button = Button(root, text = 'Select CSV from Fusemail', command = fusemail_action)
second_csv_button = Button(root, text = 'Select CSV from 365', command = active_action)
submit_button = Button(root, text = 'Submit/Process', command = process_files)
close_button = Button(root, text = 'Close Window', command = root.destroy)

first_csv_button.pack(side=tkinter.TOP)
second_csv_button.pack(side=tkinter.TOP)
submit_button.pack(side=tkinter.TOP)
close_button.pack(side=tkinter.BOTTOM)  

root.mainloop()