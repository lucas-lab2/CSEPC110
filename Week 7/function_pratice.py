import math

def compute_area_square(prompt_text):
    value = float(input(prompt_text))
    area = value ** 2
    return area

def compute_area_rectangle(l, w):
    value1 = float(input(l))
    value2 = float(input(w))
    area2 = value1 * value2
    return area2

def compute_area_circle(r):
    radius = float(input(r))
    area3 = math.pi * (radius ** 2)
    return area3


square = compute_area_square("What is the side of the square? ")
print(f"The area of the square is {square}")

rectangle = compute_area_rectangle("What is the length of the rectangle ", "What is the width of the rectangle ")
print(f"The area of the rectangle is {rectangle}")

circle = compute_area_circle("What is the radius of the circle? ")
print(f"The area of the circle is {circle: .3f}")