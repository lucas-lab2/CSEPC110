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
            while True:
        cont = int(input("Do you want try another scenario again? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
       
        break