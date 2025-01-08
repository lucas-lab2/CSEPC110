#initalize 'stop' as 1 to start the loop
stop = 1
cont = 0 

while stop == 1:
    #Ask for the user's favorite color
    color = input("What is your favorite color? ")
    print(f"Your favorite color is: {color}")
    
    #Asking the user if they want the program to keep asking
    cont = input("Do you want me to keep asking your favorite color? 1- YES 0- N0 ")
    
    #Given that the value typed by the user is a string, I used Int() in order to convert from string to interger
    stop = int(cont) 