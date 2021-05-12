import random

choices = ("rock","paper","scissor")

computer_choice = random.choice(choices)

user_choice = input("Pick rock, paper, or scissor? \n")

if user_choice == "Rock":
    if computer_choice == "rock":
        print("Tie")
    elif computer_choice == "paper":
        print("Computer Wins")
    else:
        print("User wins")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Win")
    elif computer_choice == "paper":
        print("Tie")
    else:
        print("Computer wins")
else: 
    if computer_choice == "rock":
        print("Computer Wins")
    elif computer_choice == "paper":
        print("User Wins")
    else:
        print("Tie")

