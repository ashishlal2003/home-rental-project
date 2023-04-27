from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import mysql.connector
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='ashishlal',
    database='home_rental'
)

# def func_view_property():

def back():
    root.destroy()
    os.system("python main.py")


def populate_table():
    myc = mydb.cursor()
    branch_no = branch_no_entry.get()

    sql = "SELECT p_no, Type, Rooms, Rent,Address, Name FROM prop_registration WHERE branch_no = %s"
    val = (branch_no,)
    myc.execute(sql, val)
    result = myc.fetchall()
    for row in result:
        table.insert('', 'end', values=row)
    
    mydb.commit()

    # root.destroy()
    # os.system("python main.py")


root = Tk()
root.title("View Listed Properties")
root.geometry('1100x500')

branch_no_label = Label(root, text="Branch No")
branch_no_label.place(x=50, y=50)

# telephone_number_label = Label(root, text="Telephone Number(s)")
# telephone_number_label.place(x=50, y=90)

branch_no_entry = Entry(root, width=60)
branch_no_entry.place(x=200, y=52)

# telephone_number_entry = Entry(root, width=60)
# telephone_number_entry.place(x=200, y=92)

table = ttk.Treeview(root, columns=('Property Number', 'Type', 'Rooms', 'Rent','Address', 'Name'), show='headings')
table.heading('Property Number', text='Property Number')
table.heading('Type', text='Type')
table.heading('Rooms', text='Rooms')
table.heading('Rent', text='Rent')
table.heading('Address', text='Address')
# table.heading('Owner No', text='Owner No')
table.heading('Name', text='Name')
# table.heading('Personal Address', text='Personal Address')
# table.heading('Telephone No', text='Telephone No')
# table.heading('Business Type', text='Business Type')
# table.heading('Contact Number', text='Contact Number')
# table.heading('Staff manager', text='Staff manager')
# table.heading('Branch No', text='Branch No')
# table.heading('City', text='City')
table.column('Property Number', width=10)

table.place(x=45, y=210)

xscrollbar = tk.Scrollbar(root, orient='horizontal', command=table.xview)
xscrollbar.grid(row=1, column=0, sticky='ew')
table.config(xscrollcommand=xscrollbar.set)

submit_but = Button(root, text="Submit", width=10, bg="purple", fg="white", command=populate_table)
submit_but.place(x=50, y=140)
back=Button(root, text="Back", width=10, bg="grey", fg="white", command=back).place(x=500, y=450)

root.mainloop()
