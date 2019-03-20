import os, random

os.system('clear')
print ("ROCK...PAPER...SCICCORS")
print ("-----------------------\n")
play_again = 'y'

while (play_again == 'y') :

    best_of = input ("Best of how many games to win ? ")
    best_of = int(best_of)
    player1_score = 0
    computer_score = 0
    game_number = 0

    while (player1_score <= best_of/2 and computer_score <= best_of/2):
        game_number += 1
        print(f"Game Number: {game_number}")
        player1_choice = input("Player 1: Select, rock, paper, or sciccors: ").upper()

        player2_index = random.randint(1,3)
        if player2_index == 1 :
            player2_choice = "ROCK"
        elif player2_index == 2 :
            player2_choice = "PAPER"
        elif player2_index == 3 :
            player2_choice = "SCISSORS"

        print("SHOOT...")
        print(f"Player 1 choice is {player1_choice}")
        print(f"Computer choice is {player2_choice}")
        winner = None

        if player1_choice == player2_choice :
            winner = "Draw!!!"
        elif player1_choice == "ROCK" and player2_choice == "SCISSORS":
            winner = "Player 1"
            player1_score += 1
        elif player1_choice == "PAPER" and player2_choice == "ROCK":
            winner = "Player 1"
            player1_score += 1
        elif player1_choice == "SCISSORS" and player2_choice == "PAPER":
            winner = "Player 1"
            player1_score += 1
        else:
            winner = "Computer"
            computer_score += 1
        print(f"The winner is: {winner}")
    print (f"Player 1 score is {player1_score}")
    print (f"Computer score is {computer_score}")
    if player1_score > computer_score:
        print ("Player 1 WINS !!!")
    else :
        print ("Computer WINS !!!")
    play_again = input ('Would you like to play again ? (y/n) ')

print ('OK...SEE YA!')
