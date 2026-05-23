#STRINGS:core,indexing,slicing
text = "Python is a great programming language"
print(f"value of text: {text}")
print(f"data type of text: {type(text)}") # str is a built-in data type in Python

# indexing
print(f"first character of text: {text[0]}") # indexing starts from 0
print(f"last character of text: {text[-1]}") # negative indexing starts from -1

# slicing
print(f"substring from index 0 to 5: {text[0:6]}") # slicing is done using the syntax [start:end], end index is exclusive
print(f"substring from index 11 to the end: {text[11:]}") # If end index is not provided, it goes till the end of the string
print(f"substring from the beginning to index 5: {text[:6]}") # If start index is not provided, it starts from the beginning of the string
print(f"substring from index 0 to the end with step 2: {text[0::2]}") # slicing is done using the syntax [start:end:step], step is the number of characters to skip

#immutable 
print(f"value of text: {id(text)}") # strings are immutable data types in Python, so they have a unique memory address
text = "Python is an amazing language" # when we try to modify the string, it creates a new string and assigns it to the variable, instead of modifying the original string
print(f"value of text: {text}")
print(f"value of text: {id(text)}") # the memory address of the new string is different from the original string

#encoding and decoding
encoded_text = text.encode('utf-8') # encoding the string to bytes using utf-8 encoding
print(f"encoded text: {encoded_text}")
decoded_text = encoded_text.decode('utf-8') # decoding the bytes back to string using utf-8 encoding
print(f"decoded text: {decoded_text}")


#Operations
text="Hello World"
print(f"value of text: {text*2}") # string concatenation using the * operator
print(f"value of text: {text + '!' }") # string concatenation using the + operator
print(f"value of text: {'Hello' in text}") # checking if a substring is present in the string using the in operator
print(f"value of text: {text.upper()}") # converting the string to uppercase using the
print(f"value of text: {text.lower()}") # converting the string to lowercase using the lower() method
print(f"value of text: {text.split()}") # splitting the string into a list of substrings using the split() method, by default it splits on whitespace
print(f"value of text: {text.replace('World', 'Python')}") # replacing a substring with another substring using the replace() method
