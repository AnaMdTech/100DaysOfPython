# 📝 Day 4 Notes

## ✅ What I Learned

- Learn to use conditionals in Python to check a conditions and tell the computer what to do in each case. 
- Understand the importance of indentation in Python as a way to make certain lines of code subsidiaries of other lines of code.
  - e.g.
    ``` python
      if 5 > 2: #This is a parent line of code
        print("yes") #this is a child line of code
    ``` 
- Understand how to use Comparative Operators
  - > Greater than & Less than (>, <)
  - > Greater than or equal to (>=)
  - > Less than or equal to (<=)
  - > Equal to (==)
  - > Not equal to (!=)
- Understand how Modulo works
  ``` python
  6 % 2 # will be 0
  6 % 5 # will be 1
  6 % 4 # will be 2
  ```
- Learn how to use nested statements and elif (else if) also Multiple ifs
- Learn about Logical Operators and how to use them
  ``` python
  A and B # Both conditions need to be true
  C or D # Only one condition needs to be true
  not E # The condition must be false
  ```

## 🔥 Observations

- Python conditionals (if, elif, else) play a crucial role in controlling the flow of a program based on different conditions. Mastering these will help you create dynamic programs that adapt based on user input or other factors. The importance of indentation cannot be overstated, as it defines the structure of your conditional blocks.
- Using comparative operators like >, <, ==, and != allows you to compare values and make decisions in the code. Understanding the significance of these operators ensures your program can handle various scenarios (e.g., checking if a value is greater than another or testing equality).
- The Modulo (%) operator is vital for working with remainders in divisions, which is useful for tasks such as checking if a number is even/odd or for implementing loops that cycle through certain values. The behavior of the modulo operator also helps in scenarios like counting, finding patterns, or working with intervals.
- Logical operators like and, or, and not allow you to combine multiple conditions. This is important for handling more complex decision-making. For example, checking if a number is both positive and even (using and) or if a number is either greater than 5 or less than 0 (using or).