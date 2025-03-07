import random

options = ("rock", "paper", "scissors")
game_running = True

while game_running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player= input("Enter a choice: ")

    print(f"Player: {player} ")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer =="scissors":
        print("You win!")
    elif player == "paper" and computer =="rock":
        print("You win!")
    elif player == "scissors" and computer =="paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play Again? (y/n): ").lower() == "y":
        game_running = False 
        print("Thanks for playing!")