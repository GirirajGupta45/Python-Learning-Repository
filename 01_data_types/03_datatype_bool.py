# ALL ABOUT BOOLEANS and BOOLEAN OPERATIONS
is_true = True
print(f"value of is_true: {is_true}")
print(f"data type of is_true: {type(is_true)}") # bool is a built-in data type in Python
element = 5
element=is_true+element      # upcasting bool to int for arithmetic operation
print(f"value of element: {element}")
print(f"data type of element: {type(element)}") # bool is treated as an integer in arithmetic operations

element2=10
print(f"boolean value of element2: {bool(element2)}") # any non-zero integer is considered True, while zero is considered False
element3=0
print(f"boolean value of element3: {bool(element3)}") # zero is considered False