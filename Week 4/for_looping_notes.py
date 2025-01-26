numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

print("\n")
for number in range(1, 100): #I'm defining a ranger from 1 to 11 rather than a list of numbers
    print(number)

print("\n")

for number in range(1, 100, 2): #I'm defining a ranger from 1 to 100 with a step of 2
    print(number)

print("\n")

scripture = "The Lord is my shepherd."
for letter in scripture:
    print(letter)

print("\n") 

scripture = "The Lord is my shepherd."
scripture_length = len(scripture) #I'm defining the length of the string

for i in range(scripture_length):
    print(scripture[i])
