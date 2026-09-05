# Generators and Decorators in Python

This project demonstrates two important Python concepts: **Generators** and **Decorators**.

Generators are used to produce values lazily, while decorators are used to modify or extend the behavior of functions without changing their original implementation.

---

# 📌 Generators

A generator is a special type of function that produces values **one at a time** using the `yield` keyword instead of returning all values at once.

### Characteristics

- Uses the `yield` keyword
- Produces values lazily
- Maintains its state between executions
- Reduces memory usage
- Can represent infinite sequences

### Use Cases

- Large data processing
- Reading data incrementally
- Streaming data
- Generating sequences
- Memory-efficient iteration

---

# 📌 `yield`

`yield` pauses the execution of a generator and returns a value to the caller.

When the generator is resumed, execution continues from where it was paused.

```text
Generator
    │
    ▼
yield value
    │
    ▼
Pause
    │
    ▼
next() / send()
    │
    ▼
Resume
```

---

# 📌 `next()`

The `next()` function resumes a generator and retrieves its next yielded value.

```text
next()
  ↓
Resume Generator
  ↓
Execute until yield
  ↓
Return yielded value
  ↓
Pause
```

---

# 📌 `send()`

The `send()` method is used to send a value into a paused generator.

The value becomes the result of the paused `yield` expression.

```text
Caller
   │
   │ send(value)
   ▼
Generator
   │
   ▼
yield expression
   │
   ▼
Receives value
```

---

# 📌 `yield from`

`yield from` is used to delegate values from another iterable or generator.

It allows one generator to yield values produced by another generator.

### Benefits

- Simplifies nested generator logic
- Reuses existing generators
- Improves readability
- Supports generator delegation

---

# 📌 Infinite Generator

A generator can produce values indefinitely by using a loop that never ends.

### Characteristics

- Does not store all values in memory
- Produces values only when requested
- Useful for continuous data generation
- Must be controlled by the caller

---

# 📌 `close()`

The `close()` method is used to terminate a generator before it naturally finishes.

After closing, the generator cannot continue producing values.

---

# 📌 `throw()`

The `throw()` method is used to raise an exception inside a paused generator.

It allows the caller to communicate an exception to the generator.

---

# 📌 Generator Methods

| **Method** | **Purpose** |
|------------|-------------|
| `next()` | Get the next yielded value |
| `send()` | Send a value into the generator |
| `throw()` | Raise an exception inside the generator |
| `close()` | Terminate the generator |

---

# 📌 Generators vs Normal Functions

| **Generator** | **Normal Function** |
|---------------|---------------------|
| Uses `yield` | Uses `return` |
| Produces values one at a time | Returns result at once |
| Maintains execution state | Execution ends after return |
| Memory efficient | May require more memory |
| Suitable for large or continuous data | Suitable for normal computations |

---

# 📌 Decorators

A decorator is a function that **modifies or extends the behavior of another function** without changing its original source code.

Decorators are commonly used with the `@decorator_name` syntax.

### Basic Flow

```text
Original Function
       │
       ▼
   Decorator
       │
       ▼
Modified / Extended Behavior
```

---

# 📌 How Decorators Work

A decorator generally:

- accepts a function
- defines additional behavior
- wraps the original function
- returns the wrapper function

```text
Function
   ↓
Decorator
   ↓
Wrapper
   ↓
Original Function
```

---

# 📌 `@` Decorator Syntax

Python provides a shorthand syntax for applying decorators.

```text
@decorator
def function():
    ...
```

This is conceptually equivalent to applying the decorator to the function explicitly.

---

# 📌 Common Uses of Decorators

Decorators are commonly used for:

- Logging
- Authentication and authorization
- Performance measurement
- Validation
- Caching
- Access control
- Adding reusable behavior

---

# 📌 Advantages of Decorators

- Promotes code reuse
- Separates additional behavior from core logic
- Avoids modifying the original function
- Improves maintainability
- Supports clean and modular design

---

# 📌 Generators vs Decorators

| **Generators** | **Decorators** |
|----------------|----------------|
| Produce values lazily | Modify function behavior |
| Use `yield` | Use functions as arguments |
| Maintain execution state | Wrap existing functions |
| Focus on iteration | Focus on function enhancement |
| Useful for data generation | Useful for reusable behavior |

---

# 📌 Best Practices

- Use generators when values can be produced incrementally.
- Avoid creating large collections when lazy evaluation is sufficient.
- Use `send()` only when two-way communication with a generator is actually required.
- Close generators when early termination is necessary.
- Keep decorators focused on a single responsibility.
- Use meaningful decorator names.
- Avoid excessive decorator nesting when it reduces readability.

---

# 🎯 Key Takeaway

Generators and decorators provide powerful ways to write efficient and reusable Python programs.

- `yield` → produces values lazily
- `next()` → retrieves the next value
- `send()` → sends a value into a generator
- `yield from` → delegates values to another generator
- `throw()` → raises an exception inside a generator
- `close()` → terminates a generator
- Decorators → extend or modify function behavior
- `@decorator` → applies a decorator to a function

Both concepts support **memory efficiency, code reuse, modularity, and cleaner program design**.