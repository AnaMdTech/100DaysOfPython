# Day 4 - Beginner - Control Flow and Logical Operators

## 📌 Task  

Today, we will:  

- Perform if/else statements
- Use Modulo for Even/Odd Number identifier challenge
- Learn how Nesting and elif statements works
- Understand Multiple ifs statements
- Use logical operators for decision-making. 

## 🚀 Steps  

### 1️⃣ Perform if/else statements  
``` python
age = 18
if age >= 18:
    print("You can Vote")
else:
    print("You can't Vote")
```  

### 2️⃣ Using Modulo for Even/Odd Number identifier  
``` python
num = int(input('Enter a number: '))
if num % 2 == 0:
    print(f'{num} is Even')
else:
    print(f'{num} is Odd')
```  

### 3️⃣ Nesting and elif 
``` python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
```  

### 4️⃣ Multiple ifs  
``` python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
```  

### 5️⃣ Logical Operators  
``` python
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        # Or
        # 45 <= age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
```

## 🏆 Challenge  

Modify the script to:  

- Ask the user for their height in meters and weight in kilograms.  
- Calculate and display their BMI using the formula:  
- Add a conditional statement to interpret the BMI and display the result, such as:
  - Underweight: BMI < 18.5
  - Normal weight: BMI >= 18.5 and BMI <= 24.9
  - Overweight: BMI >= 25 and BMI <= 29.9
  - Obese: BMI >= 30

    \[
    BMI = weight / height ** 2
    \]

Example:  
``` python
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")

# Interpretation of BMI
if bmi < 18.5:
    print("You are Underweight.")
elif 18.5 <= bmi <= 24.9:
    print("You have a Normal weight.")
elif 25 <= bmi <= 29.9:
    print("You are Overweight.")
else:
    print("You are Obese.")

```