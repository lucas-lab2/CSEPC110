import random

words = ["Moroni", "Lehi", "Mormon", "Prophet", "Scripture", "Liahona", "Zarahemla", "Jaredite", "Nephite"]
secret_word = random.choice(words).lower()
guesses = 0
won = False

print("Your hint is: " + "_ " * len(secret_word))

while not won:
    guess = input("Guess the word: ").lower()
    guesses += 1
    
    if len(guess) != len(secret_word):
        print(f"Please enter a {len(secret_word)}-letter word.")
        continue
    
    if guess == secret_word:
        won = True
    else:
        hint = []
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint.append(secret_word[i])  # Correct letter in the correct position
            elif guess[i] in secret_word:
                hint.append(guess[i].lower())  # Correct letter in the wrong position
            else:
                hint.append("_")  # Letter not in the word
        print("Your hint is:", " ".join(hint))

if won:
    print("\nYou won!")
else:
    print("\nYou lost!")
print(f"The word was: {secret_word}")
print(f"Number of guesses: {guesses}")