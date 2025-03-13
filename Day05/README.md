# Day 5 - Beginner - Randomisation and Python Lists

## 📌 Task  

Today, we will:  

- Use `import` keyword for inserting modules into our file
- Perform randomization using random module & its methods
- Create Lists and perform some operations
- Understand 2D Lists
- Understand how to handle IndexError
- Use `len()` for knowing number/length of items/list

## 🚀 Steps

### 1️⃣ Include `import` keyword
  ``` python
  import random
  ```

### 2️⃣ Randomization in python
``` python
import random

rand_num_0_to_1 = round(random.random())
random_float = random.uniform(1, 10) #This will generate a random floating point number between 1 and 10.
# print(rand_num_0_to_1)
# print(random_float)
if rand_num_0_to_1 == 0:
    print("Heads")
else:
    print("Tails")
```
### 3️⃣ `Lists` in python
``` python
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

states_of_america[1] = "Pencilvania"

states_of_america.append("Angelaland")

states_of_america.extend(["Angelaland", "Jack Bauer Land"])

print(states_of_america)

```

### 4️⃣ 2D Lists in python
``` python
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinach"]]
```
### 5️⃣ IndexError and len()
``` python
fruits = ["Cherry", "Apple", "Pear"]
len(fruits) #This will check length of items in the list so its 3 but python will start form 0 so it will be 2
print(fruits[3]) #This will be an IndexError lists begin from 0 so the items are 2
```

## 🏆 Challenge  

Modify the script to:  

  - Handle invalid user input in the Rock Paper Scissors game by displaying an error message if the input is not 0, 1, or 2.
  - Prevent the program from crashing when an invalid choice is made.
  - Improve the readability of the output by adding spacing and clearer messages.
  - Use a loop to allow the user to play multiple rounds until they choose to quit.
  - Implement score tracking to keep track of wins, losses, and draws.