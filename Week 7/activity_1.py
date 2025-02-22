def display_regular(message):
    display = str(input(message))
    display2 = display.upper()
    display3 = display.lower()
    return display, display2, display3


display, display2, display3 = display_regular("What is your message?")
print(f"{display}\n{display2}\n{display3}")