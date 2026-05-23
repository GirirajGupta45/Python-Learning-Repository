# Tuple (`tuple`) in Python

A tuple is an ordered collection used to store multiple values in a single variable.
Tuples are immutable, meaning their elements cannot be modified after creation.
They are commonly used for storing fixed data and ensuring data integrity.

---

# 📌 Key Characteristics

| Feature           | Description                                  |
| ----------------- | -------------------------------------------- |
| Ordered           | Elements maintain insertion order            |
| Immutable         | Values cannot be added, removed, or modified |
| Indexed           | Elements can be accessed using indexes       |
| Allows Duplicates | Duplicate values are permitted               |
| Heterogeneous     | Different datatypes can exist together       |

---

# 📌 Why Tuples are Used

* To store constant or fixed data
* To protect data from accidental modification
* Faster than lists for read-only operations
* Useful when returning multiple values from functions
* Commonly used in configurations and coordinate-like data

---

# 📌 Tuple Operations

| Operation     | Purpose                         |
| ------------- | ------------------------------- |
| Indexing      | Access element using position   |
| Slicing       | Access a range of elements      |
| Concatenation | Combine tuples                  |
| Repetition    | Repeat tuple elements           |
| Membership    | Check whether an element exists |
| Iteration     | Traverse elements one by one    |

---

# 📌 Common Tuple Functions

| Function  | Purpose                           |
| --------- | --------------------------------- |
| `len()`   | Returns number of elements        |
| `count()` | Counts occurrences of a value     |
| `index()` | Returns position of a value       |
| `max()`   | Returns largest element           |
| `min()`   | Returns smallest element          |
| `sum()`   | Returns total of numeric elements |

---

# 📌 Tuple Packing and Unpacking

## Packing

Multiple values are grouped together into a single tuple.

## Unpacking

Tuple values are extracted into separate variables.

This feature makes tuples very useful for returning and handling multiple values efficiently.

---

# 📌 Single Element Tuple

A tuple containing only one element requires a trailing comma.
Without the comma, Python treats it as a normal value instead of a tuple.

---

# 📌 Nested Tuples

Tuples can contain other tuples as elements.
This allows creation of hierarchical or grouped data structures.

---

# 📌 Tuple vs List

| Tuple             | List                     |
| ----------------- | ------------------------ |
| Immutable         | Mutable                  |
| Faster            | Slightly slower          |
| Less memory usage | More memory usage        |
| Fixed data        | Frequently changing data |

---

# 📌 Important Notes

* Tuples are immutable, but mutable objects inside them can still change.
* Tuple elements are accessed using indexes starting from `0`.
* Negative indexing is supported.
* Parentheses are optional in many cases, but recommended for readability.

---

# 🎯 Common Real-World Usage

* Returning multiple values from functions
* Storing database records
* Coordinates and geographic points
* Configuration values
* Dictionary keys (because tuples are immutable)
