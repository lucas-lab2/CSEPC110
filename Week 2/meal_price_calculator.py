"""
Author: Lucas Miranda
Purpose: Meal price calculator
"""
# Added a loop to allow users to decide if they want to run the command again 
# Added the questions about both child's and adult's drink

while True:
    # Get the price of a child's meal and drink, and the number of children
    child_meal = float(input("What is the price of a child's meal? "))
    child_drink = float(input("What is the price of a child's drink? "))
    child_number = int(input("How many children are there? "))
    
    # Get the price of an adult's meal and drink, and the number of adults
    adult_meal = float(input("\nWhat is the price of an adult's meal? "))
    adult_drink = float(input("What is the price of a adult's drink? "))
    adult_number = int(input("How many adults are there? "))
    
    # Calculate the subtotal
    subtotal = ((child_drink + child_meal) * child_number) + ((adult_drink + adult_meal) * adult_number)
    print(f"\nSubtotal: ${subtotal:.2f}")
    
    # Get the sales tax rate and calculate the tax
    sales_tax = float(input("\nWhat is the sales tax rate? "))
    tax = subtotal * (sales_tax / 100)
    print(f"Sales Tax: ${tax:.2f}")
    
    # Calculate the total cost
    total = subtotal + tax
    print(f"Total: ${total:.2f}")
    
    # Get the payment amount and calculate the change
    payment_amount = float(input("\nWhat is the payment amount? ")) 
    change = payment_amount - total
    print(f"Change: ${change:.2f}")
    
    # Ask the user if they want to continue
    while True:
        cont = int(input("Do you want to continue? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop if input is valid
        print("Invalid input. Please enter 1 or 0.")
        
    # Exit the loop if the user does not want to continue
    if cont == 0:
        break