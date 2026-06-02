#Everything About switch case in python

print("Traffic Light System")

light_color = input("Enter the traffic light color (red, yellow, green): ").lower()

match light_color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Slow down!")
    case "green":
        print("Go!")
    case _:        # _ is default case in match statement
        print("Invalid color.")