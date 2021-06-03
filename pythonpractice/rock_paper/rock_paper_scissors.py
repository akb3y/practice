import random

choices = ("rock","paper","scissor")

computer_choice = random.choice(choices)

while True:
    user_choice = input("Pick rock, paper, or scissor? \n").lower()
    if user_choice.lower() not in ("rock", "paper", "scissor"):
        print("Not an appropriate choice.")
    else:
        break

if user_choice == "rock":
    if computer_choice == "rock":
        print("\033[1;30;41m Tie! The computer had ", computer_choice, "!", sep="")
    elif computer_choice == "paper":
        print("\033[1;30;41m Computer Wins! The computer had ", computer_choice, "!", sep="")
    else:
        print("\033[1;30;41m User wins! The computer had ", computer_choice, "!", sep="")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Win! The computer had ", computer_choice, "!", sep="")
    elif computer_choice == "paper":
        print("Tie! The computer had ", computer_choice, "!", sep="")
    else:
        print("Computer wins! The computer had ", computer_choice, "!", sep="")
else:
    if computer_choice == "rock":
        print("Computer Wins! The computer had ", computer_choice, "!", sep="")
    elif computer_choice == "paper":
        print("User Wins! The computer had ", computer_choice, "!", sep="")
    else:
        print("Tie! The computer had ", computer_choice, "!", sep="")


