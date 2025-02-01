import random

words = ["Moroni", "Lehi", "Mormon", "Prophet", "Scripture", "Liahona", "Zarahemla", "Jaredite", "Nephite"]
secret_word = random.choice(words).lower()
chances = 4
won = False

print("Your hint is: " + "_ " * len(secret_word))

while chances > 0 and not won:
    guess = input("Guess the word: ").lower()
    
    if len(guess) != len(secret_word):
        print(f"Please enter a {len(secret_word)}-letter word.")
        continue
    
    if guess == secret_word:
        won = True
    else:
        hint = []
        for i in range(len(secret_word)):
            if guess[i] in secret_word:
                hint.append(guess[i])
            else:
                hint.append('_')
        print("Your hint is:", " ".join(hint))
        chances -= 1
        print(f"Chances left: {chances}")

if won:
    print("\nYou won!")
else:
    print("\nYou lost!")
    print(f"The word was: {secret_word}")