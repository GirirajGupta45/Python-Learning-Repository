def habit_generator():
    habits = [
        "Wake up early",
        "Exercise regularly",
        "Read a book",
        "Practice coding"
    ]

    while True:
        for habit in habits:
            yield habit


habits = habit_generator()

for _ in range(8):
    print(next(habits))