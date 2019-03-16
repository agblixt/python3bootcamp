import random


play_again = "y"

while play_again == "y":
    computer_number = random.randint(1,10)
    guess = None
    while guess != computer_number:
        guess = input("guess a number between 1 and 10: ")
        guess = int(guess)
        if guess > computer_number:
            print("too high")
        elif guess < computer_number:
            print("too low")
    print("Congratulations, you win")
    play_again = input("Would you like to play agiain (y/n): ")
