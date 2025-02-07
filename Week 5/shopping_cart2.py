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

    print()
    choice = input("Please enter an action: ")

    if choice == "1":
        item = input("What item would you like to add?")
        cost = float(input(f"What is the price of '{item}'? "))
        product.append(item)
        price.append(cost)
        print(f"'{item}' has been added to the cart.")
