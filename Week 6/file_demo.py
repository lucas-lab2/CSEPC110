import os
file_path = os.path.join(os.path.dirname(__file__), "courses.txt")
#courses_file = open(file_path)

with open(file_path) as courses_file:
    for line in courses_file:
        print(line)

