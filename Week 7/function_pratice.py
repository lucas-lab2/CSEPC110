def compute_area_square(prompt_text):
    value = float(input(prompt_text))
    area = value ** 2
    return area

square = compute_area_square("What is the side of the square? ")
print(f"The area of the square is {square}")

