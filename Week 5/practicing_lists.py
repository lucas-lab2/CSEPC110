names = []
new_names = ""

while new_names != "end":
    new_names = input("Type the name of a friend: ")
    new_names.lower() 
    if new_names != "end":
        names.append(new_names)

print("Your friends are:")
for name in names:
    print(name.capitalize())
