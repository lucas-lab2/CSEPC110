"""
Author: Lucas Miranda
Purpose: Grade Calculator Program
"""
while True:
    grade = float(input("What is your grade percentage? "))
    letter = 0 
    if grade < 60:
        letter = "F"
    elif grade >= 60 and grade < 70:      
        letter = "D"
    elif grade >= 70 and grade < 80:
        letter = "C"
    elif grade >= 80 and grade < 90:
        letter = "B"
    elif grade >= 90:
        letter = "A"
    
    print(f"Your grade letter is {letter} ")
    
    if grade >= 70:
        print("Congratulation, you passed the course :)! ")
    else:
         print("Unfortunately, you did not pass the course :(. But don't give, you will make it next semester! ")
    
    while True:
        cont = int(input("Do you want to convert another grade? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
        break
    