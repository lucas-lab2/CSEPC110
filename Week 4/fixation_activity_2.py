word = input("What is your favorite letter in 'Commitment'?").lower()

result = ""
"""
for letter in "Commitment":
    if letter.lower() == word:
        print(letter.upper())
    else:
        print(letter.lower())
"""

for letter in "Commitment":
    if letter.lower() == word:
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
