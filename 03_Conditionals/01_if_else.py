#ALL about if else in python
print("Welcome to the Swing Ride")
age=int(input("Enter your age: "))
if age<=5:
    print("No Ticket required")
elif age>5 and age<=12:
    print("Kids Ticket:Ticket costs 50 Rs")
elif age>12 and age<=60:
    print("Adult Ticket:Ticket costs 100 Rs")
else:
    print("You're not allowed in swing ride")
    
