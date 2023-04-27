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

window = Canvas(root, width=635, height=570, bg="#DAF5FF")
window.pack()

def back():
    root.destroy()
    os.system("python main.py")

def func_window():
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


client_registration_heading_label = Label(window, text="Client Registration Form", font=("Arial", 20, "bold"), bg="#DAF5FF", fg="#576CBC")
client_registration_heading_label.place(x=160, y=30)

client_number_label=Label(window, text="Client Number", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=50, y=50)
full_name_label=Label(window, text="Full Name", bg="#DAF5FF", fg="#394867",font=("Arial", 12)).place(x=50, y=90)
property_requirements_label=Label(window, text="Enter Property Requirements",font=("Arial", 11)).place(x=50, y=140)
type_label=Label(window, text="Type").place(x=50, y=190)
max_rent_label=Label(window, text="Max Rent").place(x=50, y=230)
branch_number_label=Label(window, text="Branch Number").place(x=50, y=280)
branch_address_label=Label(window, text="Branch Address").place(x=50, y=320)
registered_by_label=Label(window, text="Registered By").place(x=50, y=360)
date_registered_label=Label(window, text="Date Registered").place(x=50, y=400)

client_number_entry = Entry(window, width=60)
client_number_entry.place(x=200, y=52)
full_name_entry = Entry(window, width=60)
full_name_entry.place(x=200, y=92)
type_entry = Entry(window, width=60)
type_entry.place(x=200, y=192)
max_rent_entry = Entry(window, width=60)
max_rent_entry.place(x=200, y=232)
brach_number_entry = Entry(window, width=60)
brach_number_entry.place(x=200, y=282)
branch_address_entry = Entry(window, width=60)
branch_address_entry.place(x=200, y=322)
registered_by_entry = Entry(window, width=60)
registered_by_entry.place(x=200, y=362)
date_registered_entry = Entry(window, width=60)
date_registered_entry.place(x=200, y=402)


submit_but=Button(window, text="Submit", width=10, bg="purple", fg="white", command=func_window).place(x=50, y=455)
back=Button(window, text="Back", width=10, bg="grey", fg="white", command=back).place(x=485, y=455)
window.mainloop()