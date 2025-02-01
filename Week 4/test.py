import random

# List of words and corresponding hints (keys in lowercase)
words = [
    "Moroni", "Lehi", "Mormon", "Prophet", "Scripture",
    "Liahona", "Zarahemla", "Jaredite", "Nephite"
]
hints = {
    "moroni": "He is known for keeping the sacred records.",
    "lehi": "He is an early prophet who left Jerusalem.",
    "mormon": "He compiled the records into the Book of Mormon.",
    "prophet": "This word represents a messenger of God.",
    "scripture": "It refers to sacred writings.",
    "liahona": "A divine compass that guided ancient travelers.",
    "zarahemla": "Name of an ancient city mentioned in the scriptures.",
    "jaredite": "Pertains to an ancient people recorded in the Book of Mormon.",
    "nephite": "Refers to one of the ancient groups described in the scriptures."
}

# Choose a random word and convert it to lowercase for comparisons.
word = random.choice(words)
word_lower = word.lower()

# We'll use a set for the guessed letters.
letters_guessed = set()
chances = 4
won = False

while True:
    # Build the display string showing guessed letters and underscores.
    display_letters = []
    for letter in word:
        if letter.lower() in letters_guessed:
            display_letters.append(letter)
        else:
            display_letters.append("_")
    print("\n" + " ".join(display_letters))
    print(f"Chances left: {chances}")

    attempt = input("Guess a letter or the word: ").lower().strip()
    if not attempt:
        print("Please enter a guess.")
        continue

    # Process a single-letter guess.
    if len(attempt) == 1:
        if attempt not in letters_guessed:
            letters_guessed.add(attempt)
            if attempt not in word_lower:
                chances -= 1
                print("Incorrect letter!")
                print(f"Hint: {hints[word_lower]}")
        else:
            print("You already guessed that letter.")

    # Process a full-word guess.
    else:
        if attempt == word_lower:
            won = True
            break
        else:
            chances -= 1  # Deduct a chance for a wrong word guess
            print("Incorrect word guess!")
            print(f"Hint: {hints[word_lower]}")


    # Check if every letter in the secret word has been guessed.
    if all(letter.lower() in letters_guessed for letter in word):
        won = True
        break

    if chances <= 0:
        break

if won:
    print("\nYou won!")
else:
    print("\nYou lost!")
    print("The word was:", word)