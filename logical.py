citizen=(input("Enter your citizenship:"))
age=int(input("Enter your age:"))
if((citizen=="kenyan")and(age>=18)):
    print("Eligible to vote.")
else:    
    print("Not eligible.")