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

ROCK = "r"
SCISSORS = "s"
PAPER = "P"

emojis = {ROCK: "🤘" , SCISSORS: "✂️", PAPER: "🧻"}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice  = input("Rock , paper or Scisors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")
    
def determine_winner(user_choice, computer_choice):
     if user_choice == computer_choice:
         print("It's a tie!")
     elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
       print("Player win!") 
     else:
      print("Computer wins!")    
      
      
def play_game():
   while True:
     user_choice = get_user_choice()

     computer_choice = random.choice(choices)

     display_choices(user_choice, computer_choice)
 
     determine_winner(user_choice, computer_choice)

     should_continue = input('Continue? (y/n)').lower()

     if should_continue == "n":
        break           
          

play_game()    