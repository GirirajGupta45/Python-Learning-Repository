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

- To store constant or fixed data
- To protect data from accidental modification
- Faster than lists for read-only operations
- Useful when returning multiple values from functions
- Commonly used in configurations and coordinate-like data

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

# 📌 Important Notes

- Tuples are immutable, but mutable objects inside them can still change.
- Tuple elements are accessed using indexes starting from `0`.
- Negative indexing is supported.
- Parentheses are optional in many cases, but recommended for readability.

---

# 🎯 Common Real-World Usage

- Returning multiple values from functions
- Storing database records
- Coordinates and geographic points
- Configuration values
- Dictionary keys (because tuples are immutable)

---

# List (`list`) in Python

A list is an ordered and mutable collection used to store multiple values in a single variable.
Lists are one of the most commonly used datatypes in Python because they allow dynamic data manipulation.
They can store duplicate values as well as different datatypes together.

---

# 📌 Key Characteristics

| Feature           | Description                             |
| ----------------- | --------------------------------------- |
| Ordered           | Elements maintain insertion order       |
| Mutable           | Elements can be modified after creation |
| Indexed           | Elements can be accessed using indexes  |
| Allows Duplicates | Duplicate values are permitted          |
| Heterogeneous     | Different datatypes can exist together  |
| Dynamic           | Size can grow or shrink dynamically     |

---

# 📌 Why Lists are Used

- To store collections of related data
- When data needs frequent modification
- Useful for iteration and data processing
- Commonly used in loops, APIs, databases, and applications

---

# 📌 List Operations

| Operation     | Purpose                         |
| ------------- | ------------------------------- |
| Indexing      | Access element using position   |
| Slicing       | Access a range of elements      |
| Concatenation | Combine lists                   |
| Repetition    | Repeat list elements            |
| Membership    | Check whether an element exists |
| Iteration     | Traverse elements one by one    |
| Updating      | Modify existing elements        |
| Insertion     | Add new elements                |
| Deletion      | Remove elements                 |

---

# 📌 Common List Functions

| Function    | Purpose                           |
| ----------- | --------------------------------- |
| `append()`  | Adds element at end               |
| `insert()`  | Adds element at specific position |
| `extend()`  | Adds multiple elements            |
| `remove()`  | Removes specific element          |
| `pop()`     | Removes element using index       |
| `clear()`   | Removes all elements              |
| `sort()`    | Sorts the list                    |
| `reverse()` | Reverses list order               |
| `count()`   | Counts occurrences of a value     |
| `index()`   | Returns position of a value       |
| `len()`     | Returns number of elements        |

---

# 📌 Nested Lists

A list can contain other lists as elements.
This is useful for representing matrix-like or hierarchical data structures.

---

# 📌 List vs Tuple

| List            | Tuple       |
| --------------- | ----------- |
| Mutable         | Immutable   |
| Dynamic         | Fixed       |
| More flexible   | More secure |
| Slightly slower | Faster      |

---

# 📌 Important Notes

- Indexing starts from `0`.
- Negative indexing is supported.
- Lists consume more memory compared to tuples.
- Lists are mutable, so changes directly affect the original object.

---

# 🎯 Common Real-World Usage

- Storing user data
- Managing collections of items
- API responses
- Task management systems
- Data analysis and processing
- Iterative operations

# Set (`set`) in Python

A set is an unordered and mutable collection used to store unique values.
Sets automatically remove duplicate elements and are mainly used for fast membership testing and mathematical set operations.

Because sets are unordered, indexing and slicing are not supported.

---

# 📌 Key Characteristics

| Feature         | Description                                |
| --------------- | ------------------------------------------ |
| Unordered       | Elements do not maintain order             |
| Mutable         | Elements can be modified                   |
| Unique Elements | Duplicate values are automatically removed |
| Unindexed       | Indexing and slicing are not supported     |
| Fast Lookup     | Optimized for membership checking          |

---

# 📌 Why Sets are Used

- Removing duplicates
- Fast existence checking
- Comparing collections
- Performing mathematical set operations

---

# 📌 Set Operations

| Operation            | Method                   | Operator | Purpose                                |
| -------------------- | ------------------------ | -------- | -------------------------------------- |
| Union                | `union()`                | `\|`     | Combines all unique elements           |
| Intersection         | `intersection()`         | `&`      | Returns common elements                |
| Difference           | `difference()`           | `-`      | Returns unique elements from first set |
| Symmetric Difference | `symmetric_difference()` | `^`      | Returns non-common elements            |

---

# 📌 Membership Operations

| Operation            | Operator | Purpose                          |
| -------------------- | -------- | -------------------------------- |
| Membership Check     | `in`     | Checks if element exists         |
| Non-Membership Check | `not in` | Checks if element does not exist |

---

# 📌 Common Set Functions

| Function    | Purpose                    |
| ----------- | -------------------------- |
| `add()`     | Adds element               |
| `update()`  | Adds multiple elements     |
| `remove()`  | Removes specific element   |
| `discard()` | Removes element safely     |
| `pop()`     | Removes random element     |
| `clear()`   | Removes all elements       |
| `copy()`    | Creates shallow copy       |
| `len()`     | Returns number of elements |

---

# 📌 Frozen Set (`frozenset`)

A `frozenset` is an immutable version of a set.

### Characteristics

- Cannot be modified
- Supports set operations
- Can be used as dictionary keys

---

# 📌 Set vs List

| Set                | List              |
| ------------------ | ----------------- |
| Unordered          | Ordered           |
| Unique values only | Allows duplicates |
| No indexing        | Supports indexing |
| Faster lookup      | Slower lookup     |

---

# 📌 Important Notes

- Duplicate values are automatically removed.
- Sets do not maintain insertion order.
- Mutable objects cannot be stored inside sets.
- Sets are highly optimized for search and comparison operations.

---

# 🎯 Common Real-World Usage

- Removing duplicate records
- Role and permission systems
- Dataset comparison
- Search optimization
- Filtering unique values
