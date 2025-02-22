def welcome (name):
    """"Purpose: display a welcome message"""
    print (f"Hello, {name}. Welcome to the program!")

user = input("What is your name? ")  
welcome(user) # Call the function and pass the user input as an argument to the function so that the function can display the welcome message