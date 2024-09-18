#Ask the user to make a choice
#If choice is not valid
#print error
#let the computer to make a choice
#print choices (emojis)
#Determine the winner
#Ask the user   if they want to continue
# If not 
#Terminate

import random

emojis = {"r": "🤘" , "s": "✂️", "p": "🧻"}
choices = ("r", "p" , "s")

while True:
 user_choice  = input("Rock , paper or Scisors? (r/p/s): ").lower()
 if user_choice not in choices:
         print("invalid choice!")
         continue

 computer_choice = random.choice(choices)

 print(f"You chose {emojis[user_choice]}")
 print(f"Computer chose {emojis[computer_choice]}")

 if user_choice == computer_choice:
    print("It's a tie!")
 elif ((user_choice == "r" and computer_choice == "s") or
      (user_choice == "s" and computer_choice == "p") or
      (user_choice == "p" and computer_choice == "r")):
       print("Player win!") 
 else:
     print("Computer wins!")

 should_continue = input('Continue? (y/n)').lower()

 if should_continue == "n":
    break               