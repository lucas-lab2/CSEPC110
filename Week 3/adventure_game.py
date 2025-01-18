"""
Author: Lucas Miranda
Purpose: Adventure game
"""
import textwrap

while True:
    text = "You are a faithful follower of the prophet Nephi, tasked with retrieving sacred records hidden deep within the wilderness. The journey will test your faith, courage, and wisdom. As you stand at the edge of the camp, you face three paths leading into the wilderness. Which path will you take?"
    line = textwrap.fill(text, width = 50)
    print(line)
    
    choices = input("North\nEast\nWest\n")
    choices1 = choices.lower()
    choices2 = choices1 != "north" or choices1 != "east" or choices1 != "west"
    
    if choices2:
        print("Please, choose a valid option! ")
    
    
    while True:
        cont = int(input("Do you want to try a different scenario? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
        break
    