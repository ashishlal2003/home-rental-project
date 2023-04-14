from tkinter import *
import os
import mysql.connector
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='ashishlal',
    database='home_rental'
)

myc = mydb.cursor()

root = Tk()
root.title("Client Registration")
root.geometry('635x570')

def func_root():
    client_number = client_number_entry.get()
    full_name = full_name_entry.get()
    property_type = type_entry.get()
    max_rent = max_rent_entry.get()
    branch_number = brach_number_entry.get()
    branch_address = branch_address_entry.get()
    registered_by = registered_by_entry.get()
    date_registered = date_registered_entry.get()

    sql = "INSERT INTO CLIENT_REGISTRATION VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (client_number, full_name, property_type, max_rent, branch_number, branch_address, registered_by, date_registered)
    myc.execute(sql, val)
    mydb.commit()
    root.destroy()
    os.system("python main.py")

client_number_label=Label(root, text="Client Number (If known)").place(x=50, y=50)
full_name_label=Label(root, text="Full Name").place(x=50, y=90)
property_requirements_label=Label(root, text="Enter Property Requirements",font=("Arial", 11)).place(x=50, y=140)
type_label=Label(root, text="Type").place(x=50, y=190)
max_rent_label=Label(root, text="Max Rent").place(x=50, y=230)
branch_number_label=Label(root, text="Branch Number").place(x=50, y=280)
branch_address_label=Label(root, text="Branch Address").place(x=50, y=320)
registered_by_label=Label(root, text="Registered By").place(x=50, y=360)
date_registered_label=Label(root, text="Date Registered").place(x=50, y=400)

client_number_entry = Entry(root, width=60)
client_number_entry.place(x=200, y=52)
full_name_entry = Entry(root, width=60)
full_name_entry.place(x=200, y=92)
type_entry = Entry(root, width=60)
type_entry.place(x=200, y=192)
max_rent_entry = Entry(root, width=60)
max_rent_entry.place(x=200, y=232)
brach_number_entry = Entry(root, width=60)
brach_number_entry.place(x=200, y=282)
branch_address_entry = Entry(root, width=60)
branch_address_entry.place(x=200, y=322)
registered_by_entry = Entry(root, width=60)
registered_by_entry.place(x=200, y=362)
date_registered_entry = Entry(root, width=60)
date_registered_entry.place(x=200, y=402)


submit_but=Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_root).place(x=50, y=455)

root.mainloop()