"""
Author: Lucas Miranda
Purpose: Areas of Shape
"""

import math

stop = 1

while True:
    square = float(input("What is the length of a side of the square? "))
    square2 = square * square 
    print(f"The area of the square is: {square2: .1f}") 
 
    while True:
        cont = int(input("Do you want to continue? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # Sai do loop se a entrada for válida
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
        break
    

    

