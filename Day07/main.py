# main.py
# Day 7 - Beginner - Python Functions

# Defining a simple function
def greet():
    print("Hello, welcome to Day 7 of Python!")

# Calling the function
greet()

# Function with input
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python functions.")

# Calling the function with an argument
greet_user("Ana")

# Function with return value
def square(number):
    return number * number

# Calling the function and storing the result
result = square(5)
print(f"The square of 5 is {result}")
