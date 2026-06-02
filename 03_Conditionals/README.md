# Conditional Statements in Python

Conditional statements are used to control the flow of program execution based on specific conditions.

They allow a program to make decisions and execute different blocks of code depending on whether a condition evaluates to `True` or `False`.

---

# 📌 Why Conditionals are Used

Conditionals help:

- make decisions
- control program flow
- validate data
- execute logic selectively
- handle multiple scenarios

---

# 📌 `if` Statement

The `if` statement executes a block of code only when the specified condition evaluates to `True`.

### Characteristics

- Simplest conditional statement
- Evaluates a single condition
- Executes code only when the condition is satisfied

### Use Cases

- Input validation
- Permission checks
- Basic decision-making

---

# 📌 `if-else` Statement

The `if-else` statement provides two execution paths.

- One block executes when the condition is `True`
- Another block executes when the condition is `False`

### Characteristics

- Handles binary decisions
- Ensures one of the two blocks executes

### Use Cases

- Pass/Fail checks
- Login validation
- Feature toggles

---

# 📌 `if-elif-else` Statement

The `elif` (else-if) statement allows multiple conditions to be evaluated sequentially.

Python checks conditions from top to bottom and executes the first matching block.

### Characteristics

- Supports multiple decision paths
- Improves readability compared to nested `if` statements
- Stops checking after the first successful condition

### Use Cases

- Grade calculation
- Menu selection
- Category classification

---

# 📌 Nested Conditionals

A conditional statement can be placed inside another conditional statement.

### Characteristics

- Supports complex decision-making
- Allows hierarchical condition evaluation

### Drawbacks

- Excessive nesting reduces readability
- Can become difficult to maintain

---

# 📌 Switch Case in Python

Traditional switch-case statements found in languages such as Java, C++, and C# do not exist in older Python versions.

Starting from Python 3.10, Python introduced:

### Match-Case Statement

This feature provides switch-like behavior for handling multiple conditions in a cleaner and more readable way.

### Benefits

- Cleaner alternative to long `if-elif-else` chains
- Better readability
- Supports pattern matching

### Use Cases

- Menu-driven programs
- Command processing
- Event handling

---

# 📌 Ternary Operator

The ternary operator provides a compact way to write simple conditional expressions in a single line.

Instead of writing a complete `if-else` block, a value can be selected directly based on a condition.

### Characteristics

- Short and concise
- Ideal for simple conditions
- Improves readability when used appropriately

### Best Used For

- Value assignment
- Simple conditional expressions
- Short decision-making logic

### Avoid When

- Conditions become complex
- Readability starts to suffer

---

# 📌 Comparison of Conditional Constructs

| Construct        | Purpose                               |
| ---------------- | ------------------------------------- |
| `if`             | Single condition check                |
| `if-else`        | Two possible outcomes                 |
| `if-elif-else`   | Multiple conditions                   |
| Nested `if`      | Complex hierarchical conditions       |
| `match-case`     | Switch-case style decision making     |
| Ternary Operator | Short one-line conditional expression |

---

# 📌 Best Practices

- Keep conditions simple and readable.
- Prefer `if-elif-else` over excessive nested conditions.
- Use `match-case` when handling many fixed options.
- Use ternary operators only for simple decisions.
- Avoid deeply nested conditional structures.

---

# 🎯 Key Takeaway

Conditional statements form the foundation of decision-making in Python.

Python provides multiple approaches depending on complexity:

- `if` → single condition
- `if-else` → two outcomes
- `if-elif-else` → multiple outcomes
- `match-case` → switch-like behavior
- ternary operator → concise one-line decisions

Choosing the appropriate construct improves code readability, maintainability, and clarity.
