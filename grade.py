#grading program for Zetech University
num=int(input("Enter Score Obtained: "))
if (num>=70 and num<=100):
    print("Your Grade is A")
elif (num>=60 and num<=69):
    print("Your Grade is B")
elif (num>=50 and num<=59):
    print("Your Grade is C")
elif (num>=40 and num<=49):
    print("Your Grade is D")
elif (num<=39):
    print("Your Grade is E")
    print("Fail.")
    print("You're Required to take a Supplementary Examination.")
else:
    print("Invalid Score.")