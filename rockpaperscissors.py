import os, random

os.system('clear')
print ("ROCK...PAPER...SCICCORS")
player1_choice = input("Player 1: Select, rock, paper, or sciccors: ").lower()
os.system('clear')

player2_index = random.randint(1,3)
if player2_index == 1 :
    player2_choice = "rock"
elif player2_index == 2 :
    player2_choice = "paper"
elif player2_index == 3 :
    player2_choice = "scissors"

print("SHOOT...")
print(f"Player 1 choice is {player1_choice}")
print(f"Player 2 choice sis {player2_choice}")
winner = None

if player1_choice == player2_choice :
    winner = "Draw!!!"
elif player1_choice == "ROCK" and player2_choice == "SCISSORS":
    winner = "Player 1"
elif player1_choice == "PAPER" and player2_choice == "ROCK":
    winner = "Player 1"
elif player1_choice == "SCISSORS" and player2_choice == "PAPER":
    winner = "Player 1"
else:
    winner = "Player 2"
print(f"The winner is: {winner}")
