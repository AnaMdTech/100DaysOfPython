# Day 11 - Advanced - Python Functions: Decorators, Higher-Order Functions, and Closures

import time


# 1️⃣ Higher-Order Function
def apply_function(func, numbers):
    """Applies a function to each element in a list."""
    return [func(num) for num in numbers]


def square(x):
    return x * x


print(apply_function(square, [1, 2, 3, 4]))  # Output: [1, 4, 9, 16]


# 2️⃣ Closure: Function that remembers its state
def counter():
    """A function that counts how many times it is called."""
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


count_calls = counter()
print(count_calls())  # Output: 1
print(count_calls())  # Output: 2
print(count_calls())  # Output: 3


# 3️⃣ Decorator: Measuring Function Execution Time
def timing_decorator(func):
    """A decorator to measure execution time."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")
        return result

    return wrapper


@timing_decorator
def slow_function():
    """A dummy function that simulates a delay."""
    time.sleep(2)
    print("Function executed!")


slow_function()
# Output:
# Function executed!
# slow_function took 2.000xxx seconds
