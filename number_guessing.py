import random

lowest_num = 1
highest_num = 10
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Make a guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please enter a valid number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print(f"Correct! the answer was {answer}")           
            print(f"Number of guesses: {guesses}")
            is_running = False           
    else:
        print("Invalid guess")
        print(f"Please enter a valid number between {lowest_num} and {highest_num}")
    