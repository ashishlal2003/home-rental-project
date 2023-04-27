from tkinter import *
import os
root = Tk()
root.title("Property Registration")
root.geometry('630x750')
import mysql.connector
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='ashishlal',
    database='home_rental'
)

myc = mydb.cursor()

def func_root():
    sql = "INSERT INTO PROP_REGISTRATION VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
    property_number_entry.get(),
    type_entry.get(),
    rooms_entry.get(),
    rent_entry.get(),
    address_entry.get(),
    owner_number_entry.get(),
    person_business_name_entry.get(),
    person_business_address_entry.get(),
    telephone_number_entry.get(),
    type_of_business_entry.get(),
    managed_by_staff_entry.get(),
    registered_branch_entry.get(),
    city_entry.get(),
)
    myc.execute(sql,val)
    mydb.commit()
    root.destroy()
    os.system("python main.py")

property_number_label=Label(root, text="Property Number").place(x=50, y=50)
type_label=Label(root, text="Type").place(x=50, y=90)
rooms_label=Label(root, text="Rooms").place(x=400, y=90)
rent_label=Label(root, text="Rent").place(x=50, y=130)
address_label=Label(root, text="Address").place(x=50, y=170)
owner_number_label=Label(root, text="Owner Number").place(x=50, y=220)
person_business_name_label=Label(root, text="Person/Business Name").place(x=50, y=260)
person_business_address_label=Label(root, text="Person/Business Address").place(x=50, y=300)
telephone_number_label=Label(root, text="Telephone Number").place(x=50, y=340)
enter_details_label=Label(root, text="Enter details where applicable",font=("Arial", 11)).place(x=50, y=390)
type_of_business_label=Label(root, text="Type of Business").place(x=50, y=440)
managed_by_staff_label=Label(root, text="Managed By Staff").place(x=50, y=530)
registered_branch_label=Label(root, text="Registered Branch No").place(x=50, y=570)
city_label=Label(root, text="City").place(x=50, y=610)


property_number_entry=Entry(root, width=60)
property_number_entry.place(x=190, y=52)

type_entry=Entry(root, width=30)
type_entry.place(x=190, y=92)

rooms_entry=Entry(root, width=10)
rooms_entry.place(x=450, y=92)

rent_entry=Entry(root, width=60)
rent_entry.place(x=190, y=132)

address_entry=Entry(root, width=60)
address_entry.place(x=190, y=172)

owner_number_entry=Entry(root, width=60)
owner_number_entry.place(x=190, y=222)

person_business_name_entry=Entry(root, width=60)
person_business_name_entry.place(x=190, y=262)

person_business_address_entry=Entry(root, width=60)
person_business_address_entry.place(x=190, y=302)

telephone_number_entry=Entry(root, width=60)
telephone_number_entry.place(x=190, y=342)

type_of_business_entry=Entry(root, width=60)
type_of_business_entry.place(x=190, y=442)

managed_by_staff_entry=Entry(root, width=60)
managed_by_staff_entry.place(x=190, y=532)

registered_branch_entry=Entry(root, width=60)
registered_branch_entry.place(x=190, y=572)

city_entry=Entry(root, width=60)
city_entry.place(x=190, y=612)


submit_but=Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_root).place(x=50, y=650)

root.mainloop()