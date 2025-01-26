word = input("What is your favorite letter in 'Commitment'?")

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
        result += letter.upper()
    else:
        result += letter.lower()

print(result)