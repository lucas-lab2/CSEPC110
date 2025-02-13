import os

# in order to show creativity, I added the ability to run the code more than once so the user can insert another year to verify
while True:
    # Initialize variables for overall max and min
    overall_max_life = -1
    overall_min_life = float('inf') # assuming no one lives to infinity
    overall_max_country = ""
    overall_min_country = ""
    overall_max_year = 0
    overall_min_year = 0

    # Initialize variables for user's year analysis
    user_year = int(input("Enter the year of interest: "))
    user_max_life = -1
    user_min_life = float('inf')
    user_max_country = ""
    user_min_country = ""
    user_total = 0
    user_count = 0

    file_path = os.path.join(os.path.dirname(__file__), "life-expectancy.csv")

    with open(file_path) as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split(',') #   split the line by comma to get the country, year and life expectancy
            country = parts[0] # get the country
            year = int(parts[2]) #  get the year
            life = float(parts[3]) #  get the life expectancy

            # Update overall max and min
            if life > overall_max_life:
                overall_max_life = life 
                overall_max_country = country
                overall_max_year = year
            if life < overall_min_life:
                overall_min_life = life
                overall_min_country = country
                overall_min_year = year

            # Update user year stats
            if year == user_year: #  check if the year is the same as the user's year
                user_total += life
                user_count += 1
                if life > user_max_life:
                    user_max_life = life
                    user_max_country = country
                if life < user_min_life:
                    user_min_life = life
                    user_min_country = country

    # Calculate average for user's year
    user_avg = user_total / user_count if user_count > 0 else 0

    # Print overall results
    print(f"\nThe overall max life expectancy is: {overall_max_life:.3f} from {overall_max_country} in {overall_max_year}")
    print(f"The overall min life expectancy is: {overall_min_life:.3f} from {overall_min_country} in {overall_min_year}")

    # Print user year results
    if user_count > 0:
        print(f"\nFor the year {user_year}:")
        print(f"The average life expectancy across all countries was {user_avg:.2f}")
        print(f"The max life expectancy was in {user_max_country} with {user_max_life:.3f}")
        print(f"The min life expectancy was in {user_min_country} with {user_min_life:.3f}")
    else:
        print(f"\nNo data available for year {user_year}")

    # Ask user if they want to analyze another year
    response = input("\nDo you want to analyze another year? (y/n): ")
    if response.lower() != 'y':
        break