## THE PLAYER LIST SHOULD BE INTERACTIVELY CREATED AND NOT JUST SPECIFIED.
## SCORE = 19 MARKS OUT OF 22 MARKS

import time
import random

def eliminate_my_player(Gumba_Kingdom, Eliminations):
    player_to_kill = random.randint(2,6)
    player_list = Gumba_Kingdom.copy()
    for i in range(Eliminations):
        print("Next person to be Eliminated is:")
        player_to_kill = random.randint(2,6)
        print(player_list[player_to_kill])
        del player_list[player_to_kill]
        time.sleep(3)
    return tuple(player_list)

Gumba_Kindom = ["Mario", "Luigi", "Princess Peach", "Yoshi", "Bowser", "Toad", "Wario", "Donkey Kong", "Waluigi", "Shy Guy", "Diddy Kong", "Princess Daisy"]
count = 1
counter = 1

while True:
    try:
        Elimination_Total = int(input("How many players do you want to eliminate? -> "))
        if 2 <= Elimination_Total <= 6:
            break
        else:
            print("You cant use that number. Only 2-6 is available")
    except ValueError:
        print("You cant use that number. Only 2-6 is available")


Gumba_Kindom_Eliminated_Result = eliminate_my_player(Gumba_Kindom, Elimination_Total)

print(f"\nThese players remained: {Gumba_Kindom_Eliminated_Result}")
print(f"\nThese players started the game: {Gumba_Kindom}")

print("\nThese players survived the game:")
for i in range(len(Gumba_Kindom_Eliminated_Result)):
    print(f"{count} - {Gumba_Kindom_Eliminated_Result[i]}")
    count += 1

print("\nThis was the original player list:")
for i in range(len(Gumba_Kindom)):
    print(f"{counter} - {Gumba_Kindom[i]}")
    counter += 1

