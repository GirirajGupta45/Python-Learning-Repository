#from Demonstration
def morning_habits():
    yield "Wake up early"
    yield "Exercise"


def evening_habits():
    yield "Read a book"
    yield "Sleep on time"


def all_habits():
    yield from morning_habits()
    yield from evening_habits()


habits = all_habits()

for habit in habits:
    print(habit)


#close Demonstration
def habit_generator():
    try:
        yield "Wake up early"
        yield "Exercise"
        yield "Read a book"
    finally:
        print("Generator closed")


habits = habit_generator()

print(next(habits))
habits.close()