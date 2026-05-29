                                            #Rock, Paper, Scissor, Game
'''
WorkFlow OF Project:-
1.Input From User(Rock,Paper,Scissor)
2.Computer Choice(Computer Will Choose Randomly Not Conditionally)
3.Result Print

Cases:
A. Rock:
Rock-Rock=Tie
Rock-Paper=Paper Win
Rock-Scissor=Rock Win

B.Paper:
Paper-Paper=Tie
Rock-Paper=Paper Win
Scissor-Paper=Scissor Win

C.Scissor
Scissor-Scissor=Tie
Rock-Scissor=Rock Win
Paper-Scissor= Scissor

'''
import random

item_list = ["Rock", "Paper", "Scissor"]

while True:

    user_choice = input("Enter Your Move (Rock, Paper, Scissor) or Stop to quit: ")

    if user_choice == "Stop":
        print("Game Stopped")
        break

    computer_choice = random.choice(item_list)

    print(f"User Choice = {user_choice}")
    print(f"Computer Choice = {computer_choice}")

    if user_choice == computer_choice:
        print("Both chose same = Match Tie")

    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("Paper Covers Rock = Computer Wins")
        else:
            print("Rock Smashes Scissor = You Win")

    elif user_choice == "Paper":
        if computer_choice == "Scissor":
            print("Scissor Cuts Paper = Computer Wins")
        else:
            print("Paper Covers Rock = You Win")

    elif user_choice == "Scissor":
        if computer_choice == "Rock":
            print("Rock Smashes Scissor = Computer Wins")
        else:
            print("Scissor Cuts Paper = You Win")

    else:
        print("Invalid Input")

    



