from tkinter import *
import os

root = Tk()
root.title("Staff Onboarding")
root.geometry('635x700')

import mysql.connector
mydb = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='ashishlal',
    database='home_rental'
)

myc = mydb.cursor()

def back():
    root.destroy()
    os.system("python main.py")


def func_root():
    staff_number = staff_number_entry.get()
    full_name = full_name_entry.get()
    sex = sex_entry.get()
    dob = dob_entry.get()
    position = position_entry.get()
    salary = salary_entry.get()
    branch_number = branch_number_entry.get()
    # branch_address = branch_address_entry.get()
    # telephone_number_staff = telephone_number_entry.get()
    supervisor_name = supervisor_name_entry.get()
    manager_start = manager_start_entry.get()
    manager_bonus = manager_bonus_entry.get()
    sql = "INSERT INTO staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    val = (staff_number, full_name, sex, dob, position, salary, branch_number, supervisor_name, manager_start, manager_bonus)
    myc.execute(sql,val)
    mydb.commit()

    root.destroy()
    os.system("python main.py")
    

staff_number_label=Label(root, text="Staff Number").place(x=50, y=50)
full_name_label=Label(root, text="Full Name").place(x=50, y=90)
sex_label=Label(root, text="Sex").place(x=50, y=130)
dob_label=Label(root, text="DOB").place(x=50, y=170)
position_label=Label(root, text="Position").place(x=50, y=220)
salary_label=Label(root, text="salary").place(x=50, y=260)
branch_number_label=Label(root, text="Branch Number").place(x=50, y=310)
# branch_address_label=Label(root, text="Branch Address").place(x=50, y=350)
# telephone_number_label=Label(root, text="Telephone Number(s)").place(x=50, y=390)
enter_details_label=Label(root, text="Enter details where applicable",font=("Arial", 11)).place(x=50, y=440)
supervisor_name_label=Label(root, text="Supervisor Name").place(x=50, y=490)
manager_start_date_label=Label(root, text="Start Date").place(x=50, y=530)
manager_bonus_label=Label(root, text="Bonus").place(x=50, y=570)

staff_number_entry = Entry(root, width=60)
staff_number_entry.place(x=190, y=52)

full_name_entry = Entry(root, width=60)
full_name_entry.place(x=190, y=92)

sex_entry = Entry(root, width=60)
sex_entry.place(x=190, y=132)

dob_entry = Entry(root, width=60)
dob_entry.place(x=190, y=172)

position_entry = Entry(root, width=60)
position_entry.place(x=190, y=222)

salary_entry = Entry(root, width=60)
salary_entry.place(x=190, y=262)

branch_number_entry = Entry(root, width=60)
branch_number_entry.place(x=190, y=312)

# branch_address_entry = Entry(root, width=60)
# branch_address_entry.place(x=190, y=352)

# telephone_number_entry = Entry(root, width=60)
# telephone_number_entry.place(x=190, y=392)

supervisor_name_entry = Entry(root, width=60)
supervisor_name_entry.place(x=190, y=492)

manager_start_entry = Entry(root, width=60)
manager_start_entry.place(x=190, y=532)

manager_bonus_entry = Entry(root, width=60)
manager_bonus_entry.place(x=190, y=572)


submit_but=Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_root).place(x=50, y=620)
back=Button(root, text="Back", width=10, bg="grey", fg="white", command=back).place(x=475, y=620)

root.mainloop()