import os
# file_path = os.path.join(os.path.dirname(__file__), "courses.txt")
# #courses_file = open(file_path)

# with open(file_path) as courses_file: #closes the file automatically after the program runs
#     for line in courses_file:
#         print(line)

#Learning how to remove remove whitespaces 

name = "   John Doe   "
name_stripped = name.strip() #removes whitespaces from the beginning and end of the string

print(name) #prints "   John Doe   "
print(f"***{name_stripped}***") #prints John Doe

colors = "red green blue orange yellow"

color_list = colors.split() #splits the string into a list of strings

for color in color_list:
    color_stripped = color.strip()
    print(color_stripped, end=' ')
