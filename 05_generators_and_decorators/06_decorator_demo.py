def log_execution(func):
    def wrapper():
        print("Function execution started")
        func()
        print("Function execution completed")

    return wrapper


@log_execution
def greet():
    print("Hello, Gaurav!")


greet()