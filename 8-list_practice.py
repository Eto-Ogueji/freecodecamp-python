classes = ["JSS1", "JSS2", "JSS3", "SS1", "SS2", "SS3"]

age = int(input("Enter your age: "))

if age != 0:
    
    if (age <= 10) and (age <= 13):
        print("Your class ranges from " + classes[0] + " to " + classes[2])

    elif (age >=14) and (age <= 17):
        print("Your class ranges from " + classes[3] + " to " + classes[5])
