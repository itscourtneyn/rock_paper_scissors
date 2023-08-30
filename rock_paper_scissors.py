import random

moves = ['rock', 'paper', 'scissors']
computer = random.choice(moves)

def play():
    while True:
        player = input("Choose a move, 'rock', 'paper', or 'scissors'.  Enter 'I quit' at any time to leave the game. ")
        if player.lower() == 'i quit':
            print("Thank you for playing." )
            break
        print(f"The computer chose {computer} and you chose {player}.")
        if computer.lower() == player.lower():
            print("Game Tied")
        elif computer.lower()== 'paper' and player.lower()=='rock':
            print("You lose")
        elif computer.lower() == 'rock' and player.lower()== 'scissors':
            print("You lose")
        elif computer.lower() == 'scissors' and player.lower() == 'paper':
            print("You lose")
        elif computer.lower()== 'rock' and player.lower()=='paper':
            print("You win")
        elif computer.lower() == 'scissors' and player.lower()== 'rock':
            print("You win")
        elif computer.lower() == 'paper' and player.lower() == 'scissors':
            print("You win")
        else:
            print("That is not a valid move.  Please enter 'rock', 'paper', 'scissors' or 'I quit'.")

play()
