from tkinter import *
root = Tk()
root.title("Client Registration")
root.geometry('635x570')

def func_two():
    root.destroy()
    import home_page

client_number_label=Label(root, text="Client Number (If known)").place(x=50, y=50)
full_name_label=Label(root, text="Full Name").place(x=50, y=90)
property_requirements_label=Label(root, text="Enter Property Requirements",font=("Arial", 11)).place(x=50, y=140)
type_label=Label(root, text="Type").place(x=50, y=190)
max_rent_label=Label(root, text="Max Rent").place(x=50, y=230)
branch_number_label=Label(root, text="Branch Number").place(x=50, y=280)
branch_address_label=Label(root, text="Branch Address").place(x=50, y=320)
registered_by_label=Label(root, text="Registered By").place(x=50, y=360)
date_registered_label=Label(root, text="Date Registered").place(x=50, y=400)

client_number_entry=Entry(root, width=60).place(x=200, y=52)
full_name_entry=Entry(root, width=60).place(x=200, y=92)
type_entry=Entry(root, width=60).place(x=200, y=192)
max_rent_entry=Entry(root, width=60).place(x=200, y=232)
brach_number_entry=Entry(root, width=60).place(x=200, y=282)
branch_address_entry=Entry(root, width=60).place(x=200, y=322)
registered_by_entry=Entry(root, width=60).place(x=200, y=362)
date_registered_entry=Entry(root, width=60).place(x=200, y=402)

submit_but=Button(root, text="Submit", width=10, bg="purple", fg="white", command=func_two).place(x=50, y=455)

root.mainloop()