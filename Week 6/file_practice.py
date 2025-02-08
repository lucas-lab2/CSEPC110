import os

file_path = os.path.join(os.path.dirname(__file__), "books.txt")

with open(file_path) as books_file:
    for line in books_file:
        line_stripped = line.strip() #strips the line of whitespaces
        print(line_stripped) #prints the stripped line
