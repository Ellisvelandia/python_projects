# Generate a random number
#Loop
#Ask the user to make a guess
#If not a valid number
#Print an error
#If number < guess
#print too low
#if number > guess
# print too high
#Else
#Print well done


# import random

# number = random.randint(1,10)
# print("Guess the number between 1 and 10")

# while True:
#     user_guess = input("Make a guess: ")

#     if not user_guess.isdigit():
#         print("Please enter a valid number")
#         continue

#     user_guess = int(user_guess)

#     if user_guess < number:
#         print("Too low")
#     elif user_guess > number:
#         print("Too high")
#     else:
#         print("Well done!")
#         break

import random 

number_to_guess = random.randint(1,10)

while True:
   try:
      guess = int(input('Guesss the number between 1 and 10: '))
   
      if guess < number_to_guess:
        print("Too Low!")
      elif guess > number_to_guess:
          print("Too High")
      else:
          print("Congratulation! You guessed the number.")
          break          
   except ValueError:
       print("Please enter a valid number") 
  