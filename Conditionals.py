age1 = 16
student1 = "Mike D."

age2 = 13
student2 = "Jamie M."

age3 = 19
student3 = "Sam D."

#Special entity characters have a forward slash in front indicating
print(student1 + ": " + str(age1) + "Nickname: \"Mad \\Mike\'")
print(student2 + ": " + str(age2))
print(student3 + ": " + str(age3))
print(student3 + ":"  + str(age3))

#A boolean data type
college_plans = True

#binary conditional
if(college_plans):
    gpa = float(input("What is your gpa? "))
    sat = int(input("SAT score: "))
    #nested conditional
    #Check for high gpa and high SAT
    if(gpa > 3.85 and sat > 1400):
        print("Great scores. You have a good chance for a full scholarship.")
    elif(gpa >= 3.5 and sat > 1350):
        print("Nice scores. You can probably get a nice partial scholarship. ")
    elif(gpa >= 3.5 or sat > 1250):
        print("You have a good shot at acceptance.")
    else:
        print("You should pick up your scores in community college. ")
else:
    print("Good luck in the work force.")


temperature = 50

#incorrect
if(temperature > 90):
    print("Heat warning")
if(temperature> 70):
    print("warm day")
if(temperature >= 50):
    print("mild day")
if(temperature >30):
    print("Cold day")
if(temperature > 0):
    print("Freezing")



