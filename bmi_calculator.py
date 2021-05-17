#   The management at the gym you go to asked you to design an application that will calculate the
#   Body Mass Index (BMI) of gym members.
import tkinter as tkinter_module
from tkinter.ttk import Combobox

#   FUNCTION TAKES IN weight IN KG AND height IN CM AND WILL RETURN YOUR BMI
def calculate_bmi(weight, height):
    #   HERE, WE GET THE BMI BY
    #   1.)    TAKING THE height AND DIVIDING IT BY 100
    #   2.)    GET THE RESULT OF .1) AND SQUARE IT
    #   3.)    DIVIDE THE RESULT OF 2.) BY THE weight
    #   3.)    RETURN THE ANSWER ROUNDED OFF TO TWO DECIMAL PLACES
    bmi = round(weight / pow((height / 100), 2), 2)

    #   NOW, WE WANNA GET THE USERS WEIGHT STATUS
    #   IF THE bmi IS UNDER 18, THEN THE USER IS UNDERWEIGHT
    if bmi < 18:
        return "bmi: " + str(bmi) + ", your weight status: underweight"
    #   IF THE bmi IS EQUAL OR ABOVE 18, BUT LESS THEN 25, THEN THE USER IS NORMAL
    elif 18 <= bmi < 25:
        return "bmi: " + str(bmi) + ", your weight status: normal"
    #   IF THE bmi IS EQUAL OR ABOVE 25, BUT LESS THEN 30, THEN THE USER IS OVERWEIGHT
    elif 25 <= bmi < 30:
        return "bmi: " + str(bmi) + ", your weight status: overweight"
    #   IF THE bmi IS ABOVE 30, THEN THE USER IS OBESE
    else:
        return "bmi: " + str(bmi) + ", your weight status: obese"


#   FUNCTION WILL CALCULATE THE USERS IDEAL BMI
def calculate_male_ideal_bmi(weight, height):
    #   WE GET THE IDEAL BMI BY USING THE NORMAL BMI CALCULATION BUT WITH A FEW ADDITIONS
    return round(0.5 * weight / pow((height / 100), 2) + 11.5, 2)


def calculate_female_ideal_bmi(weight, height, age):
    #   WE GET THE IDEAL BMI BY USING THE NORMAL BMI CALCULATION BUT WITH A FEW ADDITIONS LIKE TAKING THE USERS AGE
    #   INTO ACCOUNT
    return round(0.5 * weight / pow((height / 100), 2) + 0.03 * age + 11, 2)


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
kilogram_label = tkinter_module.Label(info_frame, text="kilograms", fg="blue")
kilogram_label.place(x=200, y=20)

height_label = tkinter_module.Label(info_frame, text="Height:", fg="blue")
height_label.place(x=10, y=45)
height_entry = tkinter_module.Entry(info_frame, bg="white", width=15)
height_entry.place(x=65, y=45)
cm_label = tkinter_module.Label(info_frame, text="cm", fg="blue")
cm_label.place(x=200, y=45)

gender_label = tkinter_module.Label(info_frame, text="Gender:", fg="blue")
gender_label.place(x=10, y=80)
gender_entry = Combobox(info_frame, width=15)
gender_entry.place(x=65, y=80)

age_label = tkinter_module.Label(info_frame, text="Age:", fg="blue")
age_label.place(x=10, y=110)
height_entry = tkinter_module.Entry(info_frame, bg="white", width=15)
height_entry.place(x=65, y=110)

calculate_btn = tkinter_module.Button(window, text="Calculate the Ideal BMI")
calculate_btn.place(x=155, y=270)

BMI_label = tkinter_module.Label(window, text="BMI:")
BMI_label.place(x=100, y=320)
BMI_entry = tkinter_module.Entry(window, bg="white", width=10)
BMI_entry.place(x=135, y=320)






window.mainloop()