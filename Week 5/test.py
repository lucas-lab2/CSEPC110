names = []
numbers = []

# Ask the user for the number of friends
num_friends = int(input("How many friends do you want to add? "))

# Populate the lists with user input
for _ in range(num_friends):
    name = input("Enter the friend's name: ")
    number = input("Enter the friend's phone number: ")
    names.append(name)
    numbers.append(number)

# Print the names and numbers
for i in range(len(names)):
    name = names[i]
    number = numbers[i]
    print(f"{name} - {number}")
