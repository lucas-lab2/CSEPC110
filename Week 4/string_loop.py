candy = "no"

while candy == "no":
    candy = input("May I have a piece of candy? ")
    candy = candy.lower()
    
    while candy != "yes" and candy != "no":
        print("Please, insert a valid option (Yes or No)")
        candy = input("May I have a piece of candy? ").lower()
    if candy == "yes":
        print("Thank you")

       