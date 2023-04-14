from tkinter import *
import os

root = Tk()
root.title("Lease Form")
root.geometry('600x630')

def func_root():
    root.destroy()
    os.system("python main.py")

client_number_label=Label(root, text="Client Number (enter if known)").place(x=50, y=50)
full_name_label=Label(root, text="Full Name (proot print)").place(x=50, y=90)
payment_details_label=Label(root, text="Enter payment details").place(x=50, y=140)
monthly_rent_label=Label(root, text="Monthly Rent").place(x=50, y=190)
payment_method_label=Label(root, text="Payment Method").place(x=50, y=230)
deposit_paid_label=Label(root, text="Deposit Paid (Y or N)").place(x=50, y=270)
property_number_label=Label(root, text="Property Number").place(x=50, y=320)
property_address_label=Label(root, text="Property Address").place(x=50, y=360)
rent_start_label=Label(root, text="Rent Start").place(x=50, y=410)
rent_finish_label=Label(root, text="Rent Finish").place(x=50, y=450)
duration_label=Label(root, text="Duration").place(x=50, y=490)

client_number_entry=Entry(root, width=50).place(x=235, y=52)
full_name_entry=Entry(root, width=50).place(x=235, y=92)
monthly_rent_entry=Entry(root, width=20).place(x=235, y=192)
payment_method_entry=Entry(root, width=20).place(x=235, y=232)
deposit_paid_entry=Entry(root, width=3).place(x=235, y=272)
property_number_entry=Entry(root, width=50).place(x=235, y=322)
property_address_entry=Entry(root, width=50).place(x=235, y=362)
rent_start_entry=Entry(root, width=20).place(x=235, y=412)
rent_finish_entry=Entry(root, width=20).place(x=235, y=452)
duration_entry=Entry(root, width=20).place(x=235, y=492)

submit_but=Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_root).place(x=50, y=540)

root.mainloop()