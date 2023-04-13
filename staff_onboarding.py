from tkinter import *
staff_onboard = Tk()
staff_onboard.title("Staff Onboarding")
staff_onboard.geometry('635x700')

def func_staff_onboard():
    staff_onboard.quit()
    # import home_page
    

staff_number_label=Label(staff_onboard, text="Staff Number").place(x=50, y=50)
full_name_label=Label(staff_onboard, text="Full Name").place(x=50, y=90)
sex_label=Label(staff_onboard, text="Sex").place(x=50, y=130)
dob_label=Label(staff_onboard, text="DOB").place(x=50, y=170)
position_label=Label(staff_onboard, text="Position").place(x=50, y=220)
salary_label=Label(staff_onboard, text="salary").place(x=50, y=260)
branch_number_label=Label(staff_onboard, text="Branch Number").place(x=50, y=310)
branch_address_label=Label(staff_onboard, text="Branch Address").place(x=50, y=350)
telephone_number_label=Label(staff_onboard, text="Telephone Number(s)").place(x=50, y=390)
enter_details_label=Label(staff_onboard, text="Enter details where applicable",font=("Arial", 11)).place(x=50, y=440)
supervisor_name_label=Label(staff_onboard, text="Supervisor Name").place(x=50, y=490)
manager_start_date_label=Label(staff_onboard, text="Manager Start Date").place(x=50, y=530)
manager_bonus_label=Label(staff_onboard, text="Manager Bonus").place(x=50, y=570)

staff_number_entry=Entry(staff_onboard, width=60).place(x=190, y=52)
full_name_entry=Entry(staff_onboard, width=60).place(x=190, y=92)
sex_entry=Entry(staff_onboard, width=60).place(x=190, y=132)
dob_entry=Entry(staff_onboard, width=60).place(x=190, y=172)
position_entry=Entry(staff_onboard, width=60).place(x=190, y=222)
salary_entry=Entry(staff_onboard, width=60).place(x=190, y=262)
branch_number_entry=Entry(staff_onboard, width=60).place(x=190, y=312)
branch_address_entry=Entry(staff_onboard, width=60).place(x=190, y=352)
telephone_number_entry=Entry(staff_onboard, width=60).place(x=190, y=392)
supervisor_name_entry=Entry(staff_onboard, width=60).place(x=190, y=492)
manager_start_entry=Entry(staff_onboard, width=60).place(x=190, y=532)
manager_bonus_entry=Entry(staff_onboard, width=60).place(x=190, y=572)

submit_but=Button(staff_onboard, text="Submit", width=10, bg="purple", fg="white", command=func_staff_onboard).place(x=50, y=620)

staff_onboard.mainloop()