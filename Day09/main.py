# Day 9 - Advanced - Python Functions: *args, **kwargs, and Function Unpacking

# 1️⃣ Function with *args (Multiple Positional Arguments)
def sum_numbers(*args):
    """Returns the sum of all given numbers."""
    return sum(args)

print(sum_numbers(2, 4, 6))  # Output: 12
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15


# 2️⃣ Function with **kwargs (Multiple Keyword Arguments)
def person_info(**kwargs):
    """Prints out information about a person."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Ana", age=23, city="Addis Ababa")
# Output:
# name: Ana
# age: 23
# city: Adama


# 3️⃣ Argument Unpacking
def multiply(a, b, c):
    """Returns the product of three numbers."""
    return a * b * c

numbers_list = [2, 3, 4]
print(multiply(*numbers_list))  # Output: 24

numbers_dict = {"a": 5, "b": 6, "c": 7}
print(multiply(**numbers_dict))  # Output: 210
