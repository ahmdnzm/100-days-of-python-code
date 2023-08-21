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

#Write your code below this line 👇
import random

rps = [rock, paper, scissors]

print("Rock wins against scissors.")
print("Scissors win against paper.")
print("Paper wins against rock.")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("You have entered a wrong value.You lose")

else:

    print(rps[user_choice])
    print("Computer chose: ")
    print(rps[comp_choice])

    if user_choice == 0 and comp_choice == 2:
        print("You win")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose")
    elif comp_choice > user_choice:
        print("You lose")
    elif user_choice > comp_choice:
        print("You win")
    elif user_choice == comp_choice:
        print("It's a draw")