from tkinter import *
from tkinter import filedialog as fd
import tkinter
from tkinter.ttk import *
import csv
import re
import os

'''
Issues to investigate:
1. Add logic to not accept the SMTP email addresses that may show up in the 365 reports.
'''

# Reg Expression to filter out email address on the CSV sheet.
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

# Main window info and also the array declarations for the data from the sheets.
root = Tk()
root.geometry('300x100')
label = Label(root, text="CSV Selector")
root.title('CSV Comparison Tool')
fusemail_emails = []
active_emails = []

# Function to select the file and pass back the file path using tkinter askopenfilename function.
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

#function to get filename/path from the file selection function and then pass that to the get info function with filename info and the corresponding array.
def fusemail_action():
    filename = file_selection()
    if not filename: # Checks for empty string
        return 
    get_info (fusemail_emails,filename)
   
#same function as above but for the other csv files.
def active_action():
    filename = file_selection()
    if not filename: # Checks for empty string
        return 
    get_info (active_emails,filename)
    
# Gets the array to use and filename/path to use and then opens the CSV file and gets the information from the csv.
#It filters the email address using the regular expression and puts in the array.
def get_info(list_to_use,filename):
    with open (str(filename)) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            list_to_use.extend(list(filter(lambda x: re.match(regex,x),row)))
    return (list_to_use)
#Process the arrays and checks if there are emails in the fusemail array that are not in the active emails array.
def process_files():
    with open('results.txt','w') as output:
        output.write('Save this file to a directory of choice\n******************************************************************************\n')
        output.write('Items to remove from Fusemail\n******************************************************************************\n')
        for fusemail_item in fusemail_emails:
            if fusemail_item not in active_emails:
                output.write (fusemail_item)
                output.write('\n')
    os.startfile('results.txt')

# Closes program and deletes the output file for next run.
def close_program():
    os.remove('results.txt')
    root.destroy
    
# Button declarations
first_csv_button = Button(root, text = 'Select CSV from Fusemail', command = fusemail_action)
second_csv_button = Button(root, text = 'Select CSV from 365', command = active_action)
submit_button = Button(root, text = 'Submit/Process', command = process_files)
close_button = Button(root, text = 'Close Window', command = close_program)
# Button positioning 
first_csv_button.pack(side=tkinter.TOP)
second_csv_button.pack(side=tkinter.TOP)
submit_button.pack(side=tkinter.TOP)
close_button.pack(side=tkinter.BOTTOM)  
# Loops the tkinter application window until the closed button is clicked or the X button.
root.mainloop()

