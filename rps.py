import sys
import random
from enum import Enum

# We have used Enum to show what user and computer has chosen 
class RPS(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

flag=True
while(flag):
    
    playerChoice = int(input("\nEnter....\n1 for Rock\n2 for Paper\n3 for Scissors\n\n"))

    # sys.exit() is used to end game if choice entered is not in 1,2,3.
    if playerChoice < 1 or playerChoice > 3:
        sys.exit("You must enter 1,2 or 3 only..")

    # We have used random to generate rock, paper or scissor from computer
    computerChoice = int(random.choice("123"))

    print("\nYou chose " + str(RPS(playerChoice)).replace("RPS.","") + ".")
    print("Computer chose " + str(RPS(computerChoice)).replace("RPS.","") + ".\n")    

    if playerChoice == 1 and computerChoice == 3:
        print("✨ You Win !!✨\n")
    elif playerChoice == 2 and computerChoice == 1:
        print("✨ You Win !!✨\n")
    elif playerChoice == 3 and computerChoice == 2:
        print("✨ You Win !!✨\n")
    elif playerChoice == computerChoice:
        print("🤷‍♀️ Game Tie !!🤷‍♀️ \n")
    else:
        print("💫 Computer Win !!💫\n")

    playAgain=input("Want to play again? \nPress 'Y' to continue.. \nPress Enter to exit..\n")
    if playAgain.lower()=="y":
        continue
    else:
        print("\n 🌼🌻 Thank You 🌻🌼 \n")
        flag=False
sys.exit("Good Bye 👋 \n")