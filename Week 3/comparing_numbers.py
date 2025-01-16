"""
Author: Lucas Miranda
Purpose: Areas of Shape
"""

number1 = int(input("What is the first integer number? "))
number2 = int(input("What is the second integer number? "))

if number1 > number2: 
    print(f"The first number is greater")
    print(f"The numbers are not equal")
    print(f"The second number is not greater")
elif number1 == number2:
    print(f"The first number is not greater")
    print(f"Both numbers are equal")
    print(f"The second number is not greater")
else:
    print(f"The first number is not greater")
    print(f"The numbers are not equal")
    print(f"The second number is greater")
    
animal = input("What is your favorite animal? ")
animal_lc = animal.lower()

if animal_lc == "cat":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")