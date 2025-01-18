"""
Author: Lucas Miranda
Purpose: Adventure game
"""
import textwrap
#level 1
while True:
    text = "You are a faithful follower of the prophet Nephi, tasked with retrieving sacred records hidden deep within the wilderness. The journey will test your faith, courage, and wisdom. As you stand at the edge of the camp, you face three paths leading into the wilderness. Which path will you take?"
    line = textwrap.fill(text, width=50)
    print(line)

    while True:
        choices = input("NORTH\nEAST\nWEST\n")
        choices1 = choices.upper()

        if choices1 not in ["NORTH", "EAST", "WEST"]:
            print("Please, choose a valid option!")
        else:
            break
    print(f"You chose {choices1}. Now let's proceed!\n")

    if choices1 == "NORTH":
        text2 = "You enter a dense forest filled with wild beasts. As night falls, you hear growling nearby. What will you do?"
        line2 = textwrap.fill(text2, width=50)
        print(line2)

        while True:
            north_choices = input("PRAY\nCLIMB\nRUN\n")
            north_choices1 = north_choices.upper()

            if north_choices1 not in ["PRAY", "CLIMB", "RUN"]:
                print("Please, choose a valid option!")
            else:
                break
        
        if north_choices1 == "PRAY":
            print("You kneel and pray for protection. A sudden light from above frightens the beasts, and you find a hidden path leading safely out of the forest.\n")
        elif north_choices1 == "CLIMB":
            print("You climb a tree to escape the danger, but you drop your provisions in the process. Though safe, you are now vulnerable to hunger.\n")
        elif north_choices1 == "RUN":
            print("You run blindly through the forest, escaping the growls but becoming lost in the darkness. You feel isolated and unsure of your direction.\n")   

    elif choices1 == "EAST":
        text3 = "You find a flowing river, but it is too deep to cross on foot. You notice three possible ways to continue your journey. How will you proceed?"
        line3 = textwrap.fill(text3, width=50)
        print(line3)

        while True:
            east_choices = input("BUILD\nSWIM\nFOLLOW\n")
            east_choices1 = east_choices.upper()

            if east_choices1 not in ["BUILD", "SWIM", "FOLLOW"]:
                print("Please, choose a valid option!")
            else:
                break
        
        if east_choices1 == "BUILD":
            print("You gather wood and build a raft, praying for guidance. You cross safely and find yourself closer to the sacred hill.\n")
        elif east_choices1 == "SWIM":
            print("You brave the river's current, but the waters are strong. You lose some provisions but manage to reach the other side.\n")
        elif east_choices1 == "FOLLOW":
            print("You follow the river downstream, eventually discovering a hidden path leading you further into the wilderness.\n")   

    elif choices1 == "WEST":
        text4 = "You encounter a small group of travelers who appear friendly but carry golden idols. They offer to help you in exchange for worshiping their gods. What will you do?"
        line4 = textwrap.fill(text4, width=50)
        print(line4)

        while True:
            west_choices = input("REFUSE\nPREACH\nAGREE\n")
            west_choices1 = west_choices.upper()

            if west_choices1 not in ["REFUSE", "PREACH", "AGREE"]:
                print("Please, choose a valid option!")
            else:
                break
        
        if west_choices1 == "REFUSE":
            print("You remain true to your faith, rejecting their offer. You continue alone, but your resolve strengthens.\n")
        elif west_choices1 == "PREACH":
            print("You testify of the true God. One traveler is moved by your faith and decides to guide you, ensuring safe passage.\n")
        elif west_choices1 == "AGREE":
            print("You gain their help but feel the Spirit withdraw. The journey becomes harder as doubt clouds your heart.\n")   
    #level 2
    text5 = "You continue your journey but face a spiritual trial. As you grow weary, you feel doubts creeping into your heart. A voice whispers, 'Turn back now.' What will you do?"
    line5 = textwrap.fill(text5, width=50)
    print(line5)
    while True:
        choices_level_2 = input("PRAY\nIGNORE\nRETURN\n")
        choices_lv_2 =   choices_level_2.upper()

        if choices_lv_2 not in ["PRAY", "IGNORE", "RETURN"]:
                print("Please, choose a valid option!")
        else:
            break
        
    if choices_lv_2 == "PRAY":
        print("You kneel in humility, and the Spirit fills you with strength. The doubts vanish, and you see the sacred hill in the distance.\n")
    elif choices_lv_2 == "IGNORE":
            print("You push forward, but the doubts linger. Your steps grow heavier, and the journey takes longer.\n")
    elif choices_lv_2 == "RETURN":
        print("You turn back, abandoning the mission. The sacred records remain hidden, and the prophet mourns the lost opportunity.")   
        print("The mission fails, and the sacred records remain hidden. The Spirit withdraws, and the prophet mourns the lost opportunity.")
        break
        
    text6 = "After much hardship, you arrive at the base of the sacred hill where the plates are hidden. A powerful guard challenges your worthiness to enter. How will you proceed?"
    line6 = textwrap.fill(text6, width=50)
    print(line6)
    while True:
        choices_level_3 = input("FAST\nTESTIFY\nFIGHT\n")
        choices_lv_3 =   choices_level_3.upper()

        if choices_lv_3 not in ["FAST", "TESTIFY", "FIGHT"]:
            print("Please, choose a valid option!")
        else:
            break
        
    if choices_lv_2 == "PRAY":
            print("You kneel in humility, and the Spirit fills you with strength. The doubts vanish, and you see the sacred hill in the distance.\n")
    elif choices_lv_2 == "IGNORE":
            print("You push forward, but the doubts linger. Your steps grow heavier, and the journey takes longer.\n")
    elif choices_lv_2 == "RETURN":
        print("You turn back, abandoning the mission. The sacred records remain hidden, and the prophet mourns the lost opportunity.")   
        print("The mission fails, and the sacred records remain hidden. The Spirit withdraws, and the prophet mourns the lost opportunity.")
        break
    
    while True:
        cont = int(input("Do you want to convert another grade? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
        
    if cont == 0:
        break
    

    
    