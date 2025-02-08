import os
visits = 0
file_path = os.path.join(os.path.dirname(__file__), "traffic.csv") #creates a path to the file

with open(file_path) as web_traffic: #closes the file automatically after the program runs
    for line in web_traffic:
        line_stripped = line.strip() #removes whitespaces from the beginning and end of the string
        line_split = line_stripped.split(",") #splits the string into a list of strings

        date = line_split[0]
        visits = line_split[1]
        print(f"The date the data was accessed was on: {date}, and the total of visits were: {visits}")
    print(f"The total number of visits are: {visits}")