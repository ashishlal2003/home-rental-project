from tkinter import *
import tkinter as tk
from tkinter import ttk
import os

def func_view_property():
    root.destroy()
    os.system("python frontend\main.py")

root = Tk()
root.title("View Listed Properties")
root.geometry('1100x500')

branch_address_label=Label(root, text="Branch Address").place(x=50, y=50)
telephone_number_label=Label(root, text="Telephone Number(s)").place(x=50, y=90)

branch_address_entry=Entry(root, width=60).place(x=200, y=52)
telephone_number_entry=Entry(root, width=60).place(x=200, y=92)

table = ttk.Treeview(root, columns=('Property Number', 'Address', 'Type', 'Rooms', 'Rent'), show='headings')
table.heading('Property Number', text='Property Number')
table.heading('Address', text='Address')
table.heading('Type', text='Type')
table.heading('Rooms', text='Rooms')
table.heading('Rent', text='Rent')
table.place(x=45, y=210)
# table.pack()

submit_but=Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_view_property).place(x=50, y=140)

root.mainloop()