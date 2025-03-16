# Day 7 - Beginner - Python Functions with Inputs, Default Values, and Multiple Returns

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 7)
print(f"Sum: {result}")

# Function with a default parameter
def greet_user(name="User"):
    print(f"Hello, {name}!")

greet_user()  # Uses default value
greet_user("Ana")  # Uses provided argument

# Function with multiple return values
def divide_numbers(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

q, r = divide_numbers(10, 3)
print(f"Quotient: {q}, Remainder: {r}")
