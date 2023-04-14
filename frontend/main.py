from tkinter import *
import tkinter as tk
import os

def redirect_client_registration():
    root.destroy()
    os.system("python frontend\client_registration.py")


def redirect_property_registration():
    root.destroy()
    os.system("python frontend\property_registration.py")


def redirect_view_listed_properties():
    root.destroy()
    import view_listed_properties


def redirect_provide_comments():
    root.destroy()
    os.system("python frontend\provide_comments.py")


def redirect_staff_onboarding():
    root.destroy()
    os.system("python frontend\staff_onboarding.py")


def redirect_lease_form():
    root.destroy()
    os.system("python frontend\lease_form.py")


root = tk.Tk()
root.title("Home")
root.geometry('500x270')

label_head=tk.Label(root, text="HOME", fg="Dark Blue", font=("Arial", 12)).place(x=213, y=0)

client_registration = tk.Button(root, text="Client Registration",
                             bg="purple", fg="white", height="2", width=17, command=redirect_client_registration).place(x=90, y=50)

property_registration = tk.Button(root, text="Property Registration",
                               bg="purple", fg="white", height="2", width=17, command=redirect_property_registration).place(x=90, y=110)

staff_onboarding = tk.Button(root, text="Staff Onboarding", bg="purple",
                          fg="white", height="2", width=17, command=redirect_staff_onboarding).place(x=90, y=170)

view_listed_properties = tk.Button(root, text="View Listed Properties",
                                bg="purple", fg="white", height="2", width=17, command=redirect_view_listed_properties).place(x=260, y=50)

lease_form =tk.Button(root, text="Lease Form", bg="purple",
                    fg="white", height="2", width=17, command=redirect_lease_form).place(x=260, y=110)

provide_comments = tk.Button(root, text="Provide Comments", bg="purple",
                          fg="white", height="2", width=17, command=redirect_provide_comments).place(x=260, y=170)
root.mainloop()
