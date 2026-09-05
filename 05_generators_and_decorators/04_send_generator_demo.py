def habit_generator():
    while True:
        habit = yield "What habit should I add?"
        print("Added habit:", habit)


habits = habit_generator()

print(next(habits))              # Start the generator

print(habits.send("Wake up early"))
print(habits.send("Exercise regularly"))
print(habits.send("Practice coding"))