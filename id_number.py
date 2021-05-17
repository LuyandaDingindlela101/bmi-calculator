
name = input("Enter your name: ") # The programme returns the name and surname of the person with the DOB (Date of Birth) through the person's ID number..
surname = input("Enter your surname: ")
id_num = input("Please enter your ID number: ") #The user ID is entered
id_length_num = len(id_num) # The length of the ID is sought for

if id_length_num == 13: #If the length is 13 digits, the code continues
    print("Name: "+ name)
    print("Surname: "+ surname)
    id_year = id_num[:2] #To differentiate between the ones born during the 90s and the ones born during the 2000s.
    year_first = int (id_year[0])
    if year_first >= 0 and year_first <=1:
        print("Year: "+ "20" + str (id_year)) # The ones born during the 2000s
    elif year_first >1 and year_first <= 9:
        print("Year: " + "19" + str(id_year)) # The ones born during the 90s
    id_month = int(id_num[2:4])
    if id_month == 1: # Displaying the month in word-form instead of returning the integers
        print("Month: " + "January")
    elif id_month == 2:
        print("Month: " + "February")
    elif id_month == 3:
        print("Month: " + "March")
    elif id_month == 4:
        print("Month: " + "April")
    elif id_month == 5:
        print("Month: " + "May")
    elif id_month == 6:
        print("Month: " + "June")
    elif id_month == 7:
        print("Month: " + "July")
    elif id_month == 8:
        print("Month: " + "August")
    elif id_month == 9:
        print("Month: " + "September")
    elif id_month == 10:
        print("Month: " + "October")
    elif id_month == 11:
        print("Month: " + "November")
    elif id_month == 12:
        print("Month: " + "December")
    id_day = id_num[4:6]
    print("Day: " + str(id_day))
    id_gender = id_num[6:10]
    gender_num = int(id_gender)
    if gender_num >= 0000 and gender_num <= 4999: # Whether the person is male or female, this is the deciding range...
        print("Gender: " + "FEMALE!")
    else:
        print("Gender: " + "MALE!")
    south_african = id_num[10] # The 10th digit is sought for
    if south_african == "0": #If the 10th digit is 0, the person is an S.A citizen
        print("S.A CITIZEN!")
    elif south_african == "1": #If the 10th digit is 1, the person is a permanent resident
            print("PERMANENT CITIZEN!")
    elif south_african != 0 or south_african != 1: #If neither 0 nor 1, they are not a citizen
        print("NOT AN S.A CITIZEN!")
else:
    print("Not in range!") #If the length is less than 13 or greater, this is not an ID number