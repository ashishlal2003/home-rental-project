from tkinter import *
client_register = Tk()
client_register.title("Client Registration")
client_register.geometry('635x570')

def func_client_register():
    client_register.destroy()
    # import home_page

client_number_label=Label(client_register, text="Client Number (If known)").place(x=50, y=50)
full_name_label=Label(client_register, text="Full Name").place(x=50, y=90)
property_requirements_label=Label(client_register, text="Enter Property Requirements",font=("Arial", 11)).place(x=50, y=140)
type_label=Label(client_register, text="Type").place(x=50, y=190)
max_rent_label=Label(client_register, text="Max Rent").place(x=50, y=230)
branch_number_label=Label(client_register, text="Branch Number").place(x=50, y=280)
branch_address_label=Label(client_register, text="Branch Address").place(x=50, y=320)
registered_by_label=Label(client_register, text="Registered By").place(x=50, y=360)
date_registered_label=Label(client_register, text="Date Registered").place(x=50, y=400)

client_number_entry=Entry(client_register, width=60).place(x=200, y=52)
full_name_entry=Entry(client_register, width=60).place(x=200, y=92)
type_entry=Entry(client_register, width=60).place(x=200, y=192)
max_rent_entry=Entry(client_register, width=60).place(x=200, y=232)
brach_number_entry=Entry(client_register, width=60).place(x=200, y=282)
branch_address_entry=Entry(client_register, width=60).place(x=200, y=322)
registered_by_entry=Entry(client_register, width=60).place(x=200, y=362)
date_registered_entry=Entry(client_register, width=60).place(x=200, y=402)

submit_but=Button(client_register, text="Submit", width=10, bg="purple", fg="white", command=func_client_register).place(x=50, y=455)

client_register.mainloop()