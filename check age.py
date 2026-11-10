age_approval=input('did you have a medical cause y/n: ').strip().upper()
if age_approval=='Y' :
    print("You are allowed")
else:
    age=int(input("Enter your age: "))
    if age<18:
        print("You are allowed")
    else:
        print("You are not allowed")