import random

def get_computer_choice():
    rps = random.randrange(1,4)
    if rps == 1:
        return "Rock"
    elif rps == 2:
        return "Paper"
    elif rps == 3:
        return "Scissors"

def get_user_choice():
    while True:
        user_rps = input("Rock, Paper or Scissors?").lower()
        if user_rps == "rock" or user_rps == "r":
            return "Rock"
        elif user_rps == "paper" or user_rps == "p":
            return "Paper"
        elif user_rps == "scissors" or user_rps == "s":
            return "Scissors"

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock":
        if user_choice == "Rock":
            return "Draw"
        elif user_choice == "Paper":
            return "User wins"
        elif user_choice == "Scissors":
            return "Computer wins"
        else:
            return "None"
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            return "Computer wins"
        elif user_choice == "Paper":
            return "Draw"
        elif user_choice == "Scissors":
            return "User wins"
        else:
            return "None"
    elif computer_choice == "Scissors":
        if user_choice == "Rock":
            return "User wins"
        elif user_choice == "Paper":
            return "Computer wins"
        elif user_choice == "Scissors":
            return "Draw"
        else:
            return "None"

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    win = get_winner(computer_choice, user_choice)
    print(win)

if __name__ == "__main__":
    play()