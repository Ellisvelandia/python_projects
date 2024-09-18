#Lopp
# Ask: roll the dice? 
#if user enters Y
#Generate two random numbers
# print them
# if user enters N
# print thank you message
# termiate the program
#Else
# print invalid input message
# ask user to enter Y or N
#Modify the program so the user can specefy how dice they want to roll  

import random

while True:
    roll = input("Roll the dice? (Y/N): ").lower()

    if roll == "y":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f"{dice1}, {dice2}")
    elif roll == "n":
        print("Thank you")
        break
    else:
        print("Invalid input")
        break          
        
        