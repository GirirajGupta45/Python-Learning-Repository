def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


print_table(17)
print("-------------------")
print_table(23)
print("-------------------")
n=int(input("Enter any number: "));
print_table(n)
