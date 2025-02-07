product = []
price = []

print("Welcome to the shopping cart program!")
while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    choice = input("Please enter an action: ")
    
    if choice == "1":
        item = input("What item would you like to add? ")
        cost = float(input(f"What is the price of '{item}'? "))
        product.append(item)
        price.append(cost)
        print(f"'{item}' has been added to the cart.")
    elif choice == "2":
        print("\nThe contents of the shopping cart are:")
        for i in range(len(product)):
            print(f"{i + 1}. {product[i]} - ${price[i]:.2f}")
    elif choice == "3":
        item_number = int(input("Which item would you like to remove? ")) - 1
        if 0 <= item_number < len(product):
            removed_item = product.pop(item_number)
            removed_price = price.pop(item_number)
            print(f"'{removed_item}' has been removed from the cart.")
        else:
            print("Invalid item number.")
    elif choice == "4":
        total = sum(price)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    elif choice == "5":
        print("Thank you for using the shopping cart program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    