countries=["kenya,uganda,tanzania"]
age=int(input("Enter your age:"))
country=input("Enter your country:")
if(country not in "countries") and (age<18):
    print("Not eligible to vote.")
else:
    print("Eligible to vote.")    