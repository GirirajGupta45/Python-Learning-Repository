#DICTIONARIES in python
student_details={"name":"John","age":20,"course":"Computer Science"}
print(student_details)
print(type(student_details)) # dict is a built-in data type in Python
print(student_details["name"]) # accessing value using key
print(student_details.get("age","Not Present")) # accessing value using get() method and if not present then return "Not Present"
student_details["age"]=21 # updating value using key
print(student_details)
student_details["grade"]="A" # adding a new key-value pair to the dictionary
print(student_details)
student_details.pop("course") # removing a key-value pair from the dictionary
print(student_details)
del(student_details["grade"]) # removing a key-value pair from the dictionary using del keyword
print(student_details.keys()) # getting all the keys of the dictionary
print(student_details.values()) # getting all the values of the dictionary
print(student_details.items()) # getting all the key-value pairs of the dictionary
