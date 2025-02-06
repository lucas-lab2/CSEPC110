#index =     0      1       2         3         4
colors = ['red', 'blue', 'green', 'yellow', 'black']

colors.pop(2) # remove an item from the list
colors.insert(2, 'purple') # insert an item at a specific index
for i in range(len(colors)):
    color = colors[i]
    human_index = i + 1 # human index starts at 1
    print(f" {human_index} - {color}") # red, blue, green, yellow, black 

#You can find out how many elements are in a list, by using the len function (which is short for length) as follows: 
# number_of_books = len(books)