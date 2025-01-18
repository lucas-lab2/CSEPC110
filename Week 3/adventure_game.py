"""
Author: Lucas Miranda
Purpose: Adventure game
"""
import textwrap

while True:
    text = "You are a faithful follower of the prophet Nephi, tasked with retrieving sacred records hidden deep within the wilderness. The journey will test your faith, courage, and wisdom. As you stand at the edge of the camp, you face three paths leading into the wilderness. Which path will you take?"
    line = textwrap.fill(text, width = 50)
    print(line)
    
    while True:
        choices = input("North\nEast\nWest\n")
        choices1 = choices.lower()
    
        if choices1 not in ["north", "east", "west"]:
            print("Please, choose a valid option!")
        else:
            break
    
  
    