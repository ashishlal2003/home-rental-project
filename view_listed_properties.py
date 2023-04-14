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

def func_view_property():
    def populate_table():
        # Get a cursor object from the database connection
        mycursor = mydb.cursor()
        # branch = branch_no_entry.get()
        sql = "SELECT * FROM prop_registration"
        # val = (branch,)

        mycursor.execute(sql)
        # Execute the SELECT query to retrieve the data from the prop_registration table
        rows = mycursor.fetchall()  # Fetch all rows of the result set
        
        # Insert the retrieved data into the table
        for row in rows:
            table.insert("", "end", values=row)

    root.destroy()
    populate_table()
    os.system("python main.py")

root = Tk()
root.title("View Listed Properties")
root.geometry('1100x500')

branch_no_label = Label(root, text="Branch No")
branch_no_label.place(x=50, y=50)

telephone_number_label = Label(root, text="Telephone Number(s)")
telephone_number_label.place(x=50, y=90)

branch_no_entry = Entry(root, width=60)
branch_no_entry.place(x=200, y=52)

telephone_number_entry = Entry(root, width=60)
telephone_number_entry.place(x=200, y=92)

table = ttk.Treeview(root, columns=('Property Number', 'Address', 'Type', 'Rooms', 'Rent'), show='headings')
table.heading('Property Number', text='Property Number')
table.heading('Address', text='Address')
table.heading('Type', text='Type')
table.heading('Rooms', text='Rooms')
table.heading('Rent', text='Rent')
table.place(x=45, y=210)

submit_but = Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_view_property)
submit_but.place(x=50, y=140)

root.mainloop()
