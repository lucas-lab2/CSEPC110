item = []
new_item = ""
while new_item != "quit":
    new_item = input("Please enter the items of the shopping list (type: quit to finish):")
    if new_item != "quit":
        item.append(new_item)

print("\nThe shopping list is:")
for items in item:
    print(items)

print("\nThe shopping list with indexes is:")
for i in range(len(item)):
    items = item[i]
    human_index = i + 1
    print(f"{human_index} - {items}")

remove_item = int(input("\nWhich item would you like to remove? (Enter the index): "))
item.pop(remove_item - 1)
add_item = input("What is the new item? ")
item.append(add_item)

print("\nThe shopping list is:")
for items in item:
    print(items)