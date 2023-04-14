from tkinter import *
import os
root = Tk()
root.title("Property Registration")
root.geometry('630x750')

def func_root():
    root.destroy()
    os.system("python main.py")

property_number_label=Label(root, text="Property Number").place(x=50, y=50)
type_label=Label(root, text="Type").place(x=50, y=90)
rent_label=Label(root, text="Rent").place(x=50, y=130)
address_label=Label(root, text="Property Number").place(x=50, y=170)
owner_number_label=Label(root, text="Owner Number").place(x=50, y=220)
person_business_name_label=Label(root, text="Person/Business Name").place(x=50, y=260)
person_business_address_label=Label(root, text="Person/Business Address").place(x=50, y=300)
telephone_number_label=Label(root, text="Telephone Number").place(x=50, y=340)
enter_details_label=Label(root, text="Enter details where applicable",font=("Arial", 11)).place(x=50, y=390)
type_of_business_label=Label(root, text="Type of Business").place(x=50, y=440)
contact_name_label=Label(root, text="Contact Name").place(x=50, y=480)
managed_by_staff_label=Label(root, text="Managed By Staff").place(x=50, y=530)
registered_branch_label=Label(root, text="Registered Branch").place(x=50, y=570)
city_label=Label(root, text="City").place(x=50, y=610)


property_number_entry=Entry(root, width=60).place(x=190, y=52)
type_entry=Entry(root, width=60).place(x=190, y=92)
rent_entry=Entry(root, width=60).place(x=190, y=132)
address_entry=Entry(root, width=60).place(x=190, y=172)
owner_number_entry=Entry(root, width=60).place(x=190, y=222)
person_business_name_entry=Entry(root, width=60).place(x=190, y=262)
person_business_address_entry=Entry(root, width=60).place(x=190, y=302)
telephone_number_entry=Entry(root, width=60).place(x=190, y=342)
type_of_business_entry=Entry(root, width=60).place(x=190, y=442)
contact_name_entry=Entry(root, width=60).place(x=190, y=482)
managed_by_staff_entry=Entry(root, width=60).place(x=190, y=532)
registered_branch_entry=Entry(root, width=60).place(x=190, y=572)
city_entry=Entry(root, width=60).place(x=190, y=612)

submit_but=Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_root).place(x=50, y=650)

root.mainloop()