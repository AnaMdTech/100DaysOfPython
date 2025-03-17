# Day 10 - Advanced Python Functions: Recursion, Lambda, and Function Scope

# 1️⃣ Recursion: Factorial Function
def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120


# 2️⃣ Lambda Function: Double a Number
double = lambda x: x * 2
print(double(10))  # Output: 20


# 3️⃣ Function Scope: Global, Local, and Nonlocal Variables
x = "global"

def outer_function():
    """Demonstrates variable scope."""
    x = "outer"

    def inner_function():
        nonlocal x  # Refers to outer_function's x
        x = "inner"
        print("Inside inner function:", x)

    inner_function()
    print("Inside outer function:", x)

outer_function()
print("In global scope:", x)

# Output:
# Inside inner function: inner
# Inside outer function: inner
# In global scope: global
