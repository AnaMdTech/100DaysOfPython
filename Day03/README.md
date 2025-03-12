# Day 3: Understanding Data Types & String Manipulation  

## 📌 Task  

Today, we will:  

- Learn about different data types in Python.  
- Understand type errors and how to handle them.  
- Perform type checking and conversion.  
- Use mathematical operators for calculations.  
- Apply PEMDAS to control the order of operations.  
- Learn how to use f-strings for formatting output.  

## 🚀 Steps  

### 1️⃣ Checking Data Types  
``` python
print(type("Hello"))  # String
print(type(42))       # Integer
print(type(3.14))     # Float
print(type(True))     # Boolean
```  

### 2️⃣ Handling Type Errors & Conversion  
``` python
# Type Error Example
# print("Age: " + 25)  # ❌ This will cause an error

# Type Conversion
print("Age: " + str(25))  # ✅ Correct way to concatenate strings and numbers
```  

### 3️⃣ Mathematical Operators & PEMDAS  
``` python
print(5 + 3 * 2)  # 11 (Multiplication before addition)
print((5 + 3) * 2)  # 16 (Parentheses change the order)
print(10 / 3)  # 3.3333 (Regular division)
print(10 // 3)  # 3 (Integer division)
print(2 ** 3)  # 8 (Exponentiation)
```  

### 4️⃣ Using f-strings for Better Output Formatting  
``` python
name = "Ana"
age = 22
print(f"My name is {name} and I am {age} years old.")
```  

## 🏆 Challenge  

Modify the script to:  

- Ask the user for their height in meters and weight in kilograms.  
- Calculate and display their BMI using the formula:  

  \[
  BMI = weight / height ** 2
  \]

Example:  
``` python
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi}")
```