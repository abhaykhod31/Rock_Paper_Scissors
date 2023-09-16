import sys
import random

playerChoice = input("\nEnter....\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")

player = int(playerChoice)

# sys.exit() is used to end game if choice entered is not in 1,2,3.
if player < 1 or player > 3:
    sys.exit("You must enter 1,2 or 3 only..")

# We have used random to generate rock, paper or scissor from computer
computerChoice = random.choice("123")
computer = int(computerChoice) 

print("\nYou chose " + str(player) + ".")
print("Computer chose " + str(computer) + ".\n")

if player == 1 and computer == 3:
    print("✨ You Win !!✨\n")
elif player == 2 and computer == 1:
    print("✨ You Win !!✨\n")
elif player == 3 and computer == 2:
    print("✨ You Win !!✨\n")
elif player == computer:
    print("🤷‍♀️ Game Tie !!🤷‍♀️ \n")
else:
    print("💫 Computer Win !!💫\n")

