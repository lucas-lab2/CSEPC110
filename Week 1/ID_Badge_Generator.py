# Prompt the user to enter their information
print("Please, enter the following information:\n")

# Collect the first name, last name, and email address
fname = input("First name: ")
lname = input("Last name: ")
email_address = input("Email address: ")

# Loop to ensure valid phone number input
while True:
    phone_number = input("Phone number: ")

    # Check if the input is all digits (valid phone number)
    if phone_number.isdigit():
        # Ask for job title once phone number is valid
        job_title = input("Job title: ")
        break  # Exit the loop once a valid phone number is provided
    else:
        # Inform the user about the invalid input and ask again
        print("Invalid phone number, please insert your phone number again.\n")

# Loop to ensure valid ID number input
while True:
    ID_number = input("ID Number: ")

    # Check if the input is all digits (valid ID number)
    if ID_number.isdigit():
        break  # Exit the loop once a valid ID number is provided
    else:
        # Inform the user about the invalid input and ask again
        print("Invalid ID Number, please insert your ID Number again.\n")

# Collect additional information: hair color, eyes color, month, and training status
hair = input("Hair color: ")
eyes = input("Eyes color: ")
month = input("Month: ")
training = input("Training (Yes/No): ")

# Print the formatted ID card
print("\nThe ID Card is:")
print("----------------------------------------")

# Print the last name in uppercase and first name in capitalized format
print(f"{lname.upper()}, {fname.capitalize()}")
# Print the job title in title case
print(f"{job_title.title()}")
# Print the ID number
print(f"ID: {ID_number}\n")
# Print the email address in lowercase
print(f"{email_address.lower()}")
# Print the phone number
print(f"{phone_number}\n")

# Define a column width for formatting the output
column_width = 10

# Print hair and eyes information, with the defined column width for spacing
print(f"Hair: {hair:<{column_width}} Eyer: {eyes}")
# Print month and training information, with the defined column width for spacing
print(f"Month: {month:<{column_width}} Training: {training}")
print("----------------------------------------\n")
