import os

max_life_expectancy = 0
min_life_expectancy = 150
average_life_expectancy = 0

max_life_expectancy2 = 0
min_life_expectancy2 = 150

file_path = os.path.join(os.path.dirname(__file__), "life-expectancy.csv")

with open(file_path) as file:
    next(file)  # Skip the header line
    for line in file:
        line_stripped = line.strip() #removes whitespaces from the beginning and end of the string
        line_split = line_stripped.split(",") #splits the string into a list of strings
    
        country = line_split[0]
        code = line_split[1]
        year = line_split[2]
        life_expectancy = int(line_split[3])
        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy
            country_max = country
            year_max = year
        if life_expectancy < min_life_expectancy:
            min_life_expectancy = life_expectancy
            country_min = country
            year_min = year
        average_life_expectancy += life_expectancy

    print(f"The country with the highest life expectancy is {country_max} in {year_max} with {max_life_expectancy} years.")