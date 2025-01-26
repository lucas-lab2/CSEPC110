import random
magic_number = random.randint(1, 100)
guess_number = 0
count = 0

while guess_number != magic_number:
    guess_number = int(input("What is the guess number?"))
    if guess_number > magic_number:
        print("Lower")
        count += 1
    elif guess_number < magic_number:
        print("Higher")
        count += 1
    else:
        print("You guessed it right in", count, "tries")
        break