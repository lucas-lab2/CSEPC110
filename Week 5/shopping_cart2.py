# Author: Lucas Miranda
# This program simulates a shopping cart where users can add items, view the cart, remove items, and compute the total cost.
# In order to show creativity, I have added the ability insert the quantity of each item in the cart.
# Lists to store product details
products = []
prices = []
quantities = []

# Welcome message
print("Welcome to the shopping cart program!")

while True:
    # Display menu options
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    # Get user choice
    choice = input("Please enter an action: ")

    if choice == "1":
        # Add item to the cart
        item = input("What item would you like to add? ")
        cost = float(input(f"What is the price of '{item}'? "))
        quantity = int(input(f"How many of '{item}' would you like to add? "))
        products.append(item)
        prices.append(cost)
        quantities.append(quantity)
        print(f"{quantity} of '{item}' has been added to the cart.")
    elif choice == "2":
        # View cart contents
        print("The contents of the shopping cart are:")
        for i in range(len(products)):
            print(f"{i + 1} - {products[i]} - ${prices[i]:.2f} - Quantity: {quantities[i]}")
    elif choice == "3":
        # Remove item from the cart
        item_number = int(input("Which item would you like to remove? ")) - 1
        if 0 <= item_number < len(products):
            removed_item = products.pop(item_number)
            removed_price = prices.pop(item_number)
            removed_quantity = quantities.pop(item_number)
            print(f"{removed_quantity} of '{removed_item}' has been removed from the cart.")
        else:
            print("Invalid item number.")
    elif choice == "4":
        # Compute total cost of items in the cart
        total = sum(prices[i] * quantities[i] for i in range(len(prices)))
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    elif choice == "5":
        # Exit the program
        print("Thank you for using the shopping cart program. Goodbye!")
        break
    else:
        # Handle invalid choices
        print("Invalid choice. Please try again.")