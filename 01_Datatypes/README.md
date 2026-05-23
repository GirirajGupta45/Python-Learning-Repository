# Python Basics Cheatsheet

A quick reference for fundamental Python concepts and commonly used beginner-level functions.

---

# 📌 Printing Output

## Basic Print

```python id="q7y5m3"
print("Hello World")
```

Prints text directly to the console.

---

## Formatted Print (`f-string`)

```python id="m4a2xk"
name = "Gaurav"

print(f"My name is {name}")
```

Used to insert variables directly inside strings.

### Why use `f""`?

* Cleaner syntax
* Easy variable interpolation
* More readable than string concatenation

---

# 📌 Data Types

## Integer (`int`)

```python id="q4pw1v"
age = 21
```

Whole numbers without decimal values.

---

## Float (`float`)

```python id="qj0e6s"
price = 99.99
```

Numbers containing decimal values.

---

## String (`str`)

```python id="hrk5y2"
name = "Python"
```

Used for textual data.

---

## Boolean (`bool`)

```python id="y0v8sa"
is_logged_in = True
```

Represents `True` or `False`.

---

## List (`list`)

```python id="1rw8cx"
numbers = [1, 2, 3]
```

Ordered and mutable collection.

---

## Tuple (`tuple`)

```python id="gxt0s9"
coordinates = (10, 20)
```

Ordered but immutable collection.

---

## Set (`set`)

```python id="w5nl8t"
unique_values = {1, 2, 3}
```

Unordered collection of unique values.

---

## Dictionary (`dict`)

```python id="c9u0zh"
student = {
    "name": "Gaurav",
    "age": 21
}
```

Stores data in `key : value` pairs.

---

# 📌 Type Checking

## `type()`

```python id="pyj8ru"
x = 10

print(type(x))
```

Output:

```python id="5v86pk"
<class 'int'>
```

Used to check the datatype of a variable.

---

# 📌 Memory Reference

## `id()`

```python id="k57b6v"
x = 10

print(id(x))
```

Returns the memory reference (unique identity) of an object.

### Useful For

* Understanding object references
* Learning memory behavior in Python

---

# 📌 Taking Input

```python id="6n4h2y"
name = input("Enter your name: ")
```

Takes user input as a string.

---

# 📌 Type Conversion

## Convert String to Integer

```python id="79y8sa"
age = int("21")
```

---

## Convert Integer to String

```python id="ln5t9a"
number = str(100)
```

---

## Convert Integer to Float

```python id="v8f0zq"
price = float(10)
```

---

# 📌 Comments

## Single Line Comment

```python id="3wxt86"
# This is a comment
```

---

## Multi-line Comment

```python id="j4n3zq"
"""
This is a
multi-line comment
"""
```

---

# 📌 Variable Rules

## Valid Variable Names

```python id="q3v7xw"
name = "Python"
user_age = 21
```

---

## Invalid Variable Names

```python id="d4k1oz"
2name = "Invalid"
user-name = "Invalid"
```

---

# 📌 Multiple Assignment

```python id="a9m3vc"
x, y, z = 1, 2, 3
```

Assigns multiple values in a single line.

---

# 📌 Constants (Convention)

```python id="r7n1pk"
PI = 3.14
```

Python does not have true constants, but uppercase names are treated as constants by convention.

---

# 📌 Useful Beginner Functions

## `len()`

```python id="b3y7vf"
name = "Python"

print(len(name))
```

Returns length of an object.

---

## `range()`

```python id="8xv5ql"
range(5)
```

Generates a sequence of numbers.

---

## `help()`

```python id="eh9w4m"
help(print)
```

Displays documentation for functions or objects.

---

---------------DATA TYPES--------------------
# Integer (`int`) in Python

The `int` datatype is used to store whole numbers without decimal values.
Integers can be positive, negative, or zero.
Python supports very large integer values and provides multiple arithmetic operations on them.

---

# 📌 Integer Operators

| Operator | Description         |
| -------- | ------------------- |
| `+`      | Addition            |
| `-`      | Subtraction         |
| `*`      | Multiplication      |
| `/`      | Division            |
| `//`     | Floor Division      |
| `%`      | Modulus (Remainder) |
| `**`     | Power / Exponent    |
| `+=`     | Add and Assign      |
| `-=`     | Subtract and Assign |
| `*=`     | Multiply and Assign |

---

# 📌 Important Notes

* `/` always returns a float value.
* `//` returns only the integer part.
* Integers are immutable in Python.
* Commonly used in loops, indexing, counting, and calculations.


# String (`str`) in Python

The `str` datatype is used to store textual data in Python.
Strings are created using single quotes, double quotes, or triple quotes.
A string is an ordered and immutable sequence of characters.

---

# 📌 String Operators

| Operator | Description                      |
| -------- | -------------------------------- |
| `+`      | Concatenation (Join Strings)     |
| `*`      | Repetition                       |
| `in`     | Check Presence of Character/Word |
| `not in` | Check Absence of Character/Word  |
| `[]`     | Indexing                         |
| `[:]`    | Slicing                          |

---

# 📌 Common String Functions

| Function    | Purpose                     |
| ----------- | --------------------------- |
| `len()`     | Returns string length       |
| `lower()`   | Converts to lowercase       |
| `upper()`   | Converts to uppercase       |
| `strip()`   | Removes extra spaces        |
| `replace()` | Replaces substring          |
| `split()`   | Splits string into list     |
| `find()`    | Finds position of substring |

---

# 📌 Important Notes

* Strings are immutable in Python.
* Indexing starts from `0`.
* Strings support both positive and negative indexing.
* Frequently used in user input, file handling, APIs, and data processing.





