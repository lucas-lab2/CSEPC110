"""
Author: Lucas Miranda
Purpose: Meal price calculator
"""

import math

while True:
    child_meal = float(input("What is the price of a child's meal? "))
    child_drink = float(input("What is the price of a child's drink? "))
    child_number = int(input("How many children are there? "))
    
    adult_meal = float(input("\nWhat is the price of an adult's meal? "))
    adult_drink = float(input("What is the price of a adult's drink? "))
    adult_number = int(input("How many adults are there? "))
    
    subtotal = ((child_drink + child_meal) * child_number) + ((adult_drink + adult_meal) * adult_number)
    
    
    while True:
        cont = int(input("Do you want to continue? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
        break
    