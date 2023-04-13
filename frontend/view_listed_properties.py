import tkinter as tk
from tkinter import ttk
from tkinter import *

def func_view_property():
    view_listed_property.quit()
    # import home_page

view_listed_property = Tk()
view_listed_property.title("View Listed Properties")
view_listed_property.geometry('1100x500')

branch_address_label=Label(view_listed_property, text="Branch Address").place(x=50, y=50)
telephone_number_label=Label(view_listed_property, text="Telephone Number(s)").place(x=50, y=90)

branch_address_entry=Entry(view_listed_property, width=60).place(x=200, y=52)
telephone_number_entry=Entry(view_listed_property, width=60).place(x=200, y=92)

table = ttk.Treeview(view_listed_property, columns=('Property Number', 'Address', 'Type', 'Rooms', 'Rent'), show='headings')
table.heading('Property Number', text='Property Number')
table.heading('Address', text='Address')
table.heading('Type', text='Type')
table.heading('Rooms', text='Rooms')
table.heading('Rent', text='Rent')
table.place(x=45, y=210)
# table.pack()

submit_but=Button(view_listed_property, text="Submit", width=10, bg="purple", fg="white", command=func_view_property).place(x=50, y=140)

view_listed_property.mainloop()