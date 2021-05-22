import random

choices = ("rock","paper","scissor")

computer_choice = random.choice(choices)

user_choice = input("Pick rock, paper, or scissor? \n").lower()

if user_choice == "rock":
    if computer_choice == "rock":
        print("Tie! The computer had", computer_choice)
    elif computer_choice == "paper":
        print("Computer Wins! The computer had", computer_choice)
    else:
        print("User wins! The computer had", computer_choice)
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Win! The computer had", computer_choice)
    elif computer_choice == "paper":
        print("Tie! The computer had", computer_choice)
    else:
        print("Computer wins! The computer had", computer_choice)
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("Computer Wins! The computer had", computer_choice)
    elif computer_choice == "paper":
        print("User Wins! The computer had", computer_choice)
    else:
        print("Tie! The computer had", computer_choice)
else:
    print("Please choose from the correct list next time! Computer Wins!")

