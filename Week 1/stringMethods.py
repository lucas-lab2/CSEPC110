"""
#Will modify the input so that it will convert the information from the input to a lowecase state

email = input("What is your email address? ")
print(email.lower())

#It won't change the value of the input
print(email)

#change permantely the variable to a lowercase state
email = email.lower()
print(email)
"""

book = input ("What is the title of your favorite book? ")
print(book.capitalize()) #The first letter will be in uppercase
print(book.upper())#all the letters will be in uppercase
print(book.title())#Only the first letter of each word will be in uppercase