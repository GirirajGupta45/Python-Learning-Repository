def generate_habits():
    habits = [
        "Wake up early",
        "Exercise for 30 minutes",
        "Read a book",
        "Practice coding",
        "Sleep on time"
    ]

    for habit in habits:
        yield habit


habits = generate_habits()

print("First habit:", next(habits))
print("Second habit:", next(habits))
print("Third habit:", next(habits))

print("\nRemaining habits:")

for habit in habits:
    print(habit)