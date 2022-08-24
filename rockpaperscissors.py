import random
while True:
    user_input = input("rock paper , or scissors ")

    choices = ["rock","paper","scissors"]
    while not user_input in choices:
        print("Incorrect choice, try again")
        user_input = input("rock paper , or scissors ")
    computer = random.choice(choices)
    print(f"You : {user_input}\ncomputer : {computer}")
    if user_input == computer:
     print(f"Tie ...")
    elif user_input == "rock":
        if computer == "paper":
         print(f"{computer} covers {user_input}, you lost")
    elif  user_input == "paper":
        if computer == "rock":
            print(f"{user_input}  covers {computer} you won")
    if user_input == "scissors" and computer == "paper":
        print(f"{user_input} cuts {computer}, you won")
    elif user_input == "paper" and computer == "scissors":
        print(f"{computer} cuts {user_input}, you lost")
    elif user_input == "rock" and computer == "scissors":
        print(f"{user_input} smashes {computer} , you won")
    elif user_input == "scissors" and computer == "rock":
        print(f"{computer} smashes {user_input} , you lost")
