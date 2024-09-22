# def add_one(num):
#     if (num >= 9):
#         return num + 1
    
#     total = num + 1
#     print(total)
    
#     return add_one(total)

# add_one(0)

# value = "y"
# count = 0

# while value:
#     count += 1
#     print(count)
#     if (count == 5):
#         break
#     else:
#         value = 0
#         continue

import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    
    playerchoice = input("\nEnter \n1 rock,  \n2 for paper, or \n3 for scissors:\n\n ")
    
    if playerchoice not in ["1", "2", "3"]:
        print("Invalid choice. Please choose 1 for rock,  2 for paper, or 3 for scissors.")
        return play_rps()
    
    player = int(playerchoice)
    computerchoice = random.randint(1, 3)
    computer = int(computerchoice)
    
    print("You chose " + str(RPS(player)).replace("RPS.", "").title() + " and the computer chose " + str(RPS(computer)).replace("RPS.", "").title())
    
    if player ==  1 and computer == 3:
        print("You win!")
    elif player ==  2 and computer == 1:
        print("You win!")
    elif player ==  3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("It's a tie!")
    else:
        print("You lose!")
    
    print("Play again?")
    
    while True:
        playagain = input("(y/q) ").lower()
        if playagain not in ["y", "q"]:
            continue
        else:
            break
        
    if playagain == "y":
         return play_rps()
    else:
        print("Thanks for playing!")
        sys.exit("Bye!")
        

play_rps()        