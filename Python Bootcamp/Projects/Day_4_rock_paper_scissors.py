import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choices = ["rock", "paper", "scissors"]
art = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

computer_choice = random.randint(0, 2)

if user_choice == computer_choice:
    print("Its a draw!")
    print(f"Bot you and the computer picked {choices[user_choice]}")
    print(art[user_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
    print(choices[user_choice])
    print(art[user_choice])
    print("Computer Chose:")
    print(choices[computer_choice])
    print(art[computer_choice])
elif computer_choice > user_choice:
    print("You lose")

