"""
Author: Lucas Miranda
Purpose: Areas of Shape
"""

import math

while True:
    square = float(input("What is the length of a side of the square? "))
    area = square * square 
    print(f"The area of the square is: {area: .1f}") 
    
    length = float(input("What is the length of rectangle? "))
    width = float(input("What is the width of rectangle? "))
    area = length * width
    print(f"The area of the rectangle is: {area: .1f}")
    
    
    radius = float(input("What is the radius of the circle? "))
    area_circle = math.pi * radius**2
    print(f"The area of the circle is: {area_circle: .1f}")
    
    value = float(input("What is the value to be used? "))
    
    # Square calculus
    area_square = value ** 2
    area_circle = math.pi * (value ** 2)
    valume_cube = value ** 3
    volume_sphere = (4/3) * (math.pi * (value ** 3))
    
    print(f"Area of a square: {area_square: .1f}")
    print(f"Area of a circle: {area_circle: .1f}")
    print(f"Volume of a cube: {valume_cube: .1f}")
    print(f"Volume of a sphere: {volume_sphere: .1f}")
    
    
    
    while True:
        cont = int(input("Do you want to continue? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
        break
    

    

