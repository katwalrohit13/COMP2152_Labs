# This is the python file forWeek 2
# Rohit Kumar
import random


choices = ['rock', 'paper', 'scissors']

playerChoice = input("Enter your choice (1-rock, 2-paper, 3-scissors): ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error:")
else:
        computerChoice = random.randint(1, 3) 

        playerChoiceIndex = choices[playerChoice - 1]#=> 0,1,2
        computerChoiceIndex = choices[computerChoice - 1]
        print(playerChoiceIndex, computerChoiceIndex)

        # Determine the winner logic using if-else statements
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif (playerChoice == 1 and computerChoice == 3):
            print("Player wins! Rock crushes Scissors.")
        elif (playerChoice == 2 and computerChoice == 1):
            print("Player wins! Paper covers Rock.")
        elif (playerChoice == 3 and computerChoice == 2):
            print("Player wins! Scissors cut Paper.")
        else:
            print("You lose! Computer wins.")
       
        