fname = input("What it your first name? ")
lname = input("What it your last name? ")
email_address = input("What it your email address? ")

while True:
    phone_number = input("What is your phone number? ")

    if phone_number.isdigit() and len(phone_number) == 11:
        job_title = input("What is your job title? ")
        break
    else:
        print("Invalid phone number, please insert your phone number again.\n")

while True:
    ID_number = input("What is your ID Number? ")

    if ID_number.isdigit():
        break  # Sai do loop se for válido
    else:
        print("Invalid ID Number, please insert your ID Number again.\n")

print("\nThe ID Card is:\n")
print("----------------------------------------")

