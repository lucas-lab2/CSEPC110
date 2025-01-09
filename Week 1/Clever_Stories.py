import random  # Importing the random module to choose random words later

# Display a message prompting the user to enter the necessary words for the story
print("Please enter the following: \n")

# Ask the user to input specific types of words for the story
adjective = input("Adjective: ")  
animal = input("Animal: ")  
verb = input("Verb: ")  
exclamation = input("Exclamation: ")  
verb2 = input("Verb: ")  
verb3 = input("Verb: ")  

# Print the story using the user-provided words
print("Your Story is:\n")
print(f"""The other day, I was really in trouble. It all started when I saw a very
{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. "{exclamation.capitalize()}!" I yelled. But all
I could think to do was to {verb2.lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3.lower()}
right in front of my family.""")
# `.lower()` ensures the word is in lowercase
# `.capitalize()` capitalizes the first letter of the exclamation

# Ask the user if they want to make the story funnier in order to start a version more creative of the program
stop = input("\nDo you want to make it funnier?: Yes - 1 No- 0: ")
stop2 = int(stop)  # Convert the user's input (Yes/No) into an integer (1 or 0)

# While loop that continues if the user selects 'Yes' (1)
while stop2 == 1:
    
    print("Please enter 3 adjectives: ")
    adjectives = [input("Enter an adjective: ") for _ in range(3)] 

    print("\nPlease enter 3 animals: ")
    animal = [input("Enter an animal: ") for _ in range(3)]  

    print("\nPlease enter 5 verbs: ")
    verb = [input("Enter a verb: ") for _ in range(5)]  
    
    print("\nPlease enter 3 exclamations: \n")
    explanation = [input("Enter an exclamation: ") for _ in range(3)]  

    # Randomly choose words from the lists provided by the user
    adjectives1 = random.choice(adjectives)  
    animal1 = random.choice(animal)  
    verb1 = random.choice(verb)  
    verb2 = random.choice(verb)  
    verb3 = random.choice(verb)  
    explanation1 = random.choice(explanation)  
    
    # Print the new story with the randomly selected words
    print("Your Story is:\n")
    print(f"""The other day, I was really in trouble. It all started when I saw a very
{adjectives1.lower()} {animal1.lower()} {verb1.lower()} down the hallway. "{explanation1.capitalize()}!" I yelled. But all
I could think to do was to {verb2.lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3.lower()}
right in front of my family. \n""")
    # Each of the words inserted into the story is converted to lowercase with `.lower()`
    # The exclamation is capitalized with `.capitalize()`

    # Ask the user if they want to generate another story
    cont = input("Do you want me to generate a story like this again? Yes - 1 No- 0: ")
    stop2 = int(cont)  # If the user selects 'Yes' (1), the loop continues; otherwise, it stops
