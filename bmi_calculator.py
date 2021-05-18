#   The management at the gym you go to asked you to design an application that will calculate the
#   Body Mass Index (BMI) of gym members.
import tkinter as tkinter_module
from tkinter.ttk import Combobox
from tkinter import messagebox


#   FUNCTION RETURNS YOUR BMI
def calculate_bmi(weight, height):
    #   HERE, WE GET THE BMI BY
    #   1.)    TAKING THE height AND DIVIDING IT BY 100
    #   2.)    GET THE RESULT OF .1) AND SQUARE IT
    #   3.)    DIVIDE THE RESULT OF 2.) BY THE weight
    #   3.)    RETURN THE ANSWER ROUNDED OFF TO TWO DECIMAL PLACES

    bmi = round(weight / pow((height / 100), 2), 2)
    #   REMOVE THE CONTENTS OF THE bmi_entry BEFORE ADDING THE CORRECT bmi
    bmi_entry.delete(0, tkinter_module.END)
    #   INSERT THE bmi INTO THE bmi_entry
    bmi_entry.insert(0, bmi)

    #   NOW, WE WANNA GET THE USERS WEIGHT STATUS
    #   IF THE bmi IS UNDER 18, THEN THE USER IS UNDERWEIGHT
    if bmi < 18:
        weight_status = "Your weight status: underweight"
    #   IF THE bmi IS EQUAL OR ABOVE 18, BUT LESS THEN 25, THEN THE USER IS NORMAL
    elif 18 <= bmi < 25:
        weight_status = "Your weight status: normal"
    #   IF THE bmi IS EQUAL OR ABOVE 25, BUT LESS THEN 30, THEN THE USER IS OVERWEIGHT
    elif 25 <= bmi < 30:
        weight_status = "Your weight status: overweight"
    #   IF THE bmi IS ABOVE 30, THEN THE USER IS OBESE
    else:
        weight_status = "Your weight status: obese"

    #   SHOW THE USERS weight_status TO THE USER
    tkinter_module.messagebox.showinfo(title=None, message=weight_status)


#   FUNCTION WILL CALCULATE A MALE USERS IDEAL BMI
def calculate_male_ideal_bmi(weight, height):
    #   WE GET THE IDEAL BMI BY USING THE NORMAL BMI CALCULATION BUT WITH A FEW ADDITIONS
    bmi = round(0.5 * weight / pow((height / 100), 2) + 11.5, 2)
    #   REMOVE THE CONTENTS OF THE ideal_bmi_entry BEFORE ADDING THE CORRECT bmi
    ideal_bmi_entry.delete(0, tkinter_module.END)
    #   INSERT THE bmi INTO THE ideal_bmi_entry
    ideal_bmi_entry.insert(0, bmi)


#   FUNCTION WILL CALCULATE A FEMALE USERS IDEAL BMI
def calculate_female_ideal_bmi(weight, height, age):
    #   WE GET THE IDEAL BMI BY USING THE NORMAL BMI CALCULATION BUT WITH A FEW ADDITIONS LIKE TAKING THE USERS AGE
    #   INTO ACCOUNT
    bmi = round(0.5 * weight / pow((height / 100), 2) + 0.03 * age + 11, 2)
    #   REMOVE THE CONTENTS OF THE ideal_bmi_entry BEFORE ADDING THE CORRECT bmi
    ideal_bmi_entry.delete(0, tkinter_module.END)
    #   INSERT THE bmi INTO THE ideal_bmi_entry
    ideal_bmi_entry.insert(0, bmi)


#   FUNCTION WILL DECIDE WHICH FUNCTION WILL RUN BASED ON THE USERS gender
def calculate_ideal_bmi():
    age = int(age_entry.get())
    gender = gender_entry.get()
    weight = int(weight_entry.get())
    height = int(height_entry.get())

    #   RUNT THE calculate_bmi FUNCTION
    calculate_bmi(weight, height)

    #   IF THE USER SELECTED "Male", RUN calculate_male_ideal_bmi FUNCTION
    if gender.lower() == "male":
        calculate_male_ideal_bmi(weight, height)
    #   IF THE USER SELECTED "Female", RUN calculate_female_ideal_bmi FUNCTION
    else:
        calculate_female_ideal_bmi(weight, height, age)


#   FUNCTION WILL CLEAR ALL THE ENTRIES
def clear_entries():
    bmi_entry.delete(0, tkinter_module.END)
    weight_entry.delete(0, tkinter_module.END)
    height_entry.delete(0, tkinter_module.END)
    gender_entry.delete(0, tkinter_module.END)
    ideal_bmi_entry.delete(0, tkinter_module.END)
    ideal_bmi_entry.delete(0, tkinter_module.END)


#   FUNCTION WILL CLOSE THE PROGRAM
def exit_program():
    alert_box = tkinter_module.messagebox.askquestion('Exit Application', 'Are you sure you want to exit?')
    if alert_box == 'yes':
        window.destroy()


window = tkinter_module.Tk()
window.title("Ideal Body Mass Index")
window.geometry("500x500")

heading = tkinter_module.Label(window, text="Ideal Body Mass Index Calculator", fg="blue")
heading.place(x=150, y=0)

sub_heading = tkinter_module.Label(window, text="Enter Weight, Height, Age and Gender", fg="blue")
sub_heading.place(x=135, y=30)

info_frame = tkinter_module.LabelFrame(window, width="300", height="175")
info_frame.place(x=110, y=80)

weight_label = tkinter_module.Label(info_frame, text="Weight:", fg="blue")
weight_label.place(x=10, y=20)
weight_entry = tkinter_module.Entry(info_frame, bg="white", width=15)
weight_entry.place(x=65, y=20)
kilogram_label = tkinter_module.Label(info_frame, text="kg", fg="blue")
kilogram_label.place(x=200, y=20)

height_label = tkinter_module.Label(info_frame, text="Height:", fg="blue")
height_label.place(x=10, y=45)
height_entry = tkinter_module.Entry(info_frame, bg="white", width=15)
height_entry.place(x=65, y=45)
cm_label = tkinter_module.Label(info_frame, text="cm", fg="blue")
cm_label.place(x=200, y=45)

gender_label = tkinter_module.Label(info_frame, text="Gender:", fg="blue")
gender_label.place(x=10, y=80)
gender_entry = Combobox(info_frame, width=15, value=["Male", "Female"])
gender_entry.place(x=65, y=80)

age_label = tkinter_module.Label(info_frame, text="Age:", fg="blue")
age_label.place(x=10, y=110)
age_entry = tkinter_module.Entry(info_frame, bg="white", width=15)
age_entry.place(x=65, y=110)

calculate_btn = tkinter_module.Button(window, text="Calculate the Ideal BMI", command=calculate_ideal_bmi)
calculate_btn.place(x=155, y=270)

bmi_label = tkinter_module.Label(window, text="bmi:", fg="blue")
bmi_label.place(x=100, y=320)
bmi_entry = tkinter_module.Entry(window, bg="white", width=10)
bmi_entry.place(x=135, y=320)

ideal_bmi_label = tkinter_module.Label(window, text="Ideal bmi:", fg="blue")
ideal_bmi_label.place(x=250, y=320)
ideal_bmi_entry = tkinter_module.Entry(window, bg="white", width=10)
ideal_bmi_entry.place(x=320, y=320)

clear_btn = tkinter_module.Button(window, text="Clear Entries", command=clear_entries, fg="blue")
clear_btn.place(x=100, y=380)

exit_btn = tkinter_module.Button(window, text="Exit program", command=exit_program, fg="blue")
exit_btn.place(x=300, y=380)

window.mainloop()
