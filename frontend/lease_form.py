from tkinter import *
lease = Tk()
lease.title("Lease Form")
lease.geometry('600x630')

def func_lease():
    lease.quit()
    # import home_page

client_number_label=Label(lease, text="Client Number (enter if known)").place(x=50, y=50)
full_name_label=Label(lease, text="Full Name (please print)").place(x=50, y=90)
payment_details_label=Label(lease, text="Enter payment details").place(x=50, y=140)
monthly_rent_label=Label(lease, text="Monthly Rent").place(x=50, y=190)
payment_method_label=Label(lease, text="Payment Method").place(x=50, y=230)
deposit_paid_label=Label(lease, text="Deposit Paid (Y or N)").place(x=50, y=270)
property_number_label=Label(lease, text="Property Number").place(x=50, y=320)
property_address_label=Label(lease, text="Property Address").place(x=50, y=360)
rent_start_label=Label(lease, text="Rent Start").place(x=50, y=410)
rent_finish_label=Label(lease, text="Rent Finish").place(x=50, y=450)
duration_label=Label(lease, text="Duration").place(x=50, y=490)

client_number_entry=Entry(lease, width=50).place(x=235, y=52)
full_name_entry=Entry(lease, width=50).place(x=235, y=92)
monthly_rent_entry=Entry(lease, width=20).place(x=235, y=192)
payment_method_entry=Entry(lease, width=20).place(x=235, y=232)
deposit_paid_entry=Entry(lease, width=3).place(x=235, y=272)
property_number_entry=Entry(lease, width=50).place(x=235, y=322)
property_address_entry=Entry(lease, width=50).place(x=235, y=362)
rent_start_entry=Entry(lease, width=20).place(x=235, y=412)
rent_finish_entry=Entry(lease, width=20).place(x=235, y=452)
duration_entry=Entry(lease, width=20).place(x=235, y=492)

submit_but=Button(lease, text="Submit", width=10, bg="purple", fg="white", command=func_lease).place(x=50, y=540)

lease.mainloop()