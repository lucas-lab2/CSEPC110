def get_positive_value(prompt_text):
    value = float(input(prompt_text))
    while value <= 0:
        print("Please enter a positive value.")
        value = float(input(prompt_text))
    return value


length = get_positive_value("Enter the length of the rectangle: ")
width =  get_positive_value("Enter the width of the rectangle: ")

area = length * width
print(f"The area of the rectangle is {area} square units.")



