#Practice with Numeric Variables 

age = int(input("How old are you? ")) + 1
print("On your next birthday, you will be " + str(age))

egg = int(input("\nHow many egg cartons do you have? ")) * 12
print("You have " + str(egg))

cookie = float(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))

cookie_people = cookie/people 

print(f"Each person may have {cookie_people:.2f} cookies.")