import os

file_name = os.path.join(os.path.dirname(__file__), "hr_system.txt")

with open(file_name) as hr_file:
    for line in hr_file:
        line_stripped = line.strip()
        line_split = line_stripped.split()
        name = line_split[0]
        id_number = line_split[1]
        role = line_split[2]
        salary = line_split[3]
        print(f"{name} (ID: {id_number}), {role} - ${salary} annually.")