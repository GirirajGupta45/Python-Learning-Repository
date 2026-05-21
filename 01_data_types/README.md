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

# 📌 Quick Summary

| Concept   | Purpose           |
| --------- | ----------------- |
| `print()` | Display output    |
| `f""`     | Formatted strings |
| `type()`  | Check datatype    |
| `id()`    | Memory identity   |
| `input()` | Take user input   |
| `len()`   | Length of object  |
| `range()` | Generate sequence |

---

# 🎯 Key Takeaway

Python emphasizes:

* readability
* simplicity
* minimal syntax

Understanding these basics builds the foundation for advanced concepts like OOP, decorators, frameworks, and automation.
