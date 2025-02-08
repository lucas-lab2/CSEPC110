people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

max_age = 0
oldest_person = ""
minimum_age = 100 # assuming no one is older than 100
youngest_person = ""
for person in people:
    name = person.split(",")[0]
    age = int(person.split()[1])    
    print(f"{name} is {age} years old.")
    if age > max_age:
        max_age = age
        oldest_person = name

    if age < minimum_age:
        minimum_age = age
        youngest_person = name
print(f"The oldest person is {oldest_person} and they are {max_age} years old.") 
print(f"The youngest person is {youngest_person} and they are {minimum_age} years old.")
    