import random

words = ["Moroni", "Lehi", "Mormon", "Prophet", "Scripture", "Liahona", "Zarahemla", "Jaredite", "Nephite"]
word = random.choice(words)
letter_guessed = []
chances = 4
won = False

while True:
    for letter in word:
        if letter.lower() in letter_guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print(f"\nChances left: {chances}") 
    attempt = input("Guess the word: ").lower()

    if len(attempt) == 1:
        if attempt not in letter_guessed:
            letter_guessed.append(attempt)
        if attempt not in word:
            chances -= 1
    elif attempt == word:
        won = True
        break
    else:
        for letter in attempt:
            if letter not in letter_guessed:
                letter_guessed.append(letter)
        if attempt != word:
            chances -= 1

    won = True
    for letter in word:
        if letter.lower() not in letter_guessed:
            won = False
        
    if chances == 0 or won:
        break
     
if won:
    print("\nYou won!")
else:
    print("\nYou lost!")
    print("\nThe word was:", word)
