import random

print("Please enter the following: ")

adjective = input("Adjective: ")
animal = input("Animal: ")
verb = input("Verb: ")
exclamation = input("Exclmation: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")

print("Your Story is:\n")
print(f"""The other day, I was really in trouble. It all started when I saw a very
{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all
I could think to do was to {verb2.lower()} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3.lower()}
right in front of my family.""")

while True:
    stop = input("\nDo you want to make ir funnier?: Yes - 1 No- 0: ")
    stop2 = int(stop)
    if stop2 == 0:
        break
    else:
        print("Please enter 3 adjectives: ")
        adjectives = [input("Enter an adjective: ") for _ in range(3)]

        print("Please enter 3 adjectives: ")
        adjectives = [input("Enter an adjective: ") for _ in range(3)]
    