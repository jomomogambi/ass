num=int(input("Enter amount:"))
if(num>=1000):
    print(num-(0.05*num))
    print("Discount of 5% offered.")
else:    
    print("No discount.")