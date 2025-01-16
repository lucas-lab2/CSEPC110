"""
Author: Lucas Miranda
Purpose: Areas of Shape
"""

number1 = int(input("What is the first integer number? "))
number2 = int(input("What is the second integer number? "))

if number1 > number2: 
    print(f"The first number is greater")
elif number1 == number2:
    print(f"Both numbers are equal")
else:
    print(f"The second number is greater")