import time

print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 ''')

print("\t\tWELCOME TO TREASURE ISLAND")
print("\t\t\tYour goal is to find the treasure")
time.sleep(2)

print("Chapter 1 : Crossroads")
print(''' 
        ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠻⠿⢿⣿⣿⣿⣿⡿⠿⠟⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⢸⡇⢸⡇⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣷⣄⠀⠀⠈⠛⢿⣿⣿⣿⣿⣶⣾⡇⢸⣷⣶⣿⣿⣿⣿⡿⠛⠁⠀⠀⣠⣾⣿
        ⣿⣿⣿⣷⣄⠀⠀⠀⠈⠻⢿⣿⣿⣿⡇⢸⣿⣿⣿⡿⠟⠁⠀⠀⠀⣠⣾⣿⣿⣿
        ⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠙⠻⣿⣷⣾⣿⠟⠋⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣯⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣽⣿⣿⣿⣿⣿
''')
road_choice = input("There is a cross roads up ahead do you go right or left? ->")

time.sleep(1)

if road_choice == ("right"):
    print("You made the right choice and proceeded forward!")
    time.sleep(2)
    print("Chapter 2 : Boat")
    print(''' 
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⠿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿
    ⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿
    ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
    ⣿⠀⠀⣀⣀⣀⣀⣠⣤⣤⣤⣿⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿
    ⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠉⠉⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠉⠉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠛⠂⠀⠀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣦⣤⣀⡀⠐⠒⠢⢤⣄⡀⠀⠀⠈⠉⠉⠙⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡉⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⡀⠀⠀⡠⠞⠃⠀⣠⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡏⠀⠀⣆⠀⠀⠻⣄⠀⠀⠀⣄⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣧⣤⣤⣬⣷⣤⣤⣤⣵⣤⣤⣬⣿⣦⣤⣤⣤⣤⣬⣭⣿⣿⣿⣿
        ''')
    print("You have approached a river!")
    print("There is a river ahead do you wait for the boat or swim?")
    river_choice = input("wait or swim? ->")
    if river_choice == "wait":
        print("You made the right choice and proceeded forward!")
        time.sleep(2)
        print("Chapter 3 : Doors")
        print(''' 
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
        ''')
        print("You arrive at three doors!")
        print("They are coloured red, yellow and blue")
        door_choice = input("which colour do you pick? ->")

        if door_choice == "yellow":
            print("Hooray you found the tresure!")
            print("YOU WIN !!!!!!!!!!!!!")
            print(''' 
            *******************************************************************************
                    |                   |                  |                     |
            _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                    |                `"=._o`"=._      _`"=._                     |
            _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                    |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
            _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/[     ]
            *******************************************************************************
            ''')
        else:
            print("You fell through a hole on the floor!")
            time.sleep(1)
            print("GAME OVER")
            time.sleep(1)
    else:
        print("The current draged you too fast and you cracked your skull on a rock")
        time.sleep(1)
        print("GAME OVER")
        time.sleep(1)
else:
    print("A tree fell on you and crushed your head")
    time.sleep(1)
    print("GAME OVER")
    time.sleep(1)