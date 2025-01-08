print("Please, enter the following information:\n")
fname = input("First name: ")
lname = input("Last name: ")
email_address = input("Email address: ")

while True:
    phone_number = input("Phone number: ")

    if phone_number.isdigit():
        job_title = input("Job title: ")
        break
    else:
        print("Invalid phone number, please insert your phone number again.\n")

while True:
    ID_number = input("ID Number: ")

    if ID_number.isdigit():
        break  # Sai do loop se for válido
    else:
        print("Invalid ID Number, please insert your ID Number again.\n")

print("\nThe ID Card is:")
print("----------------------------------------")
print(f"{lname.upper()}, {fname.capitalize()}")
print(f"{job_title.title()}")
print(f"ID: {ID_number}\n\n")
print(f"{email_address.lower()}")
print(f"{phone_number}")
print("----------------------------------------\n")



