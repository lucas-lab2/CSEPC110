"""
Author: Lucas Miranda
Purpose: Ask the user their name and print on the screnn
"""

#First part of the activity
name1 = input("What is your frist name? ")
name1 = name1.capitalize()

name2 = input("What is your last name? ")
name2 = name2.capitalize()

print(f"Your name is {name2}, {name1} {name2}.")

#Second part of the activity
name1 = input("What is your frist name? ")

name2 = input("What is your last name? ")

print(f"Your name is {name2.title()}, {name1.title()} {name2.title()}.")