# message = "Hello world"
# print(message)

# greetings = "Ellis is awesome"
# print(greetings)

# game_score = 2
# health = 87.5
# game_on = True

# print(game_score , health , game_on)

# name = input("What is your name? ").title()
# print(name)

# price = 10

# print(not price > 10)

# user = input("Ente your name: ").title()

# if user == "Ellis":
#     print("Welcome back " + user)
# elif user == "Crisanto":
#     print("Welcome back " + user)    
# else:
#     print("User doesn't exist")    

#Your task is to create a simple age checker for a roller coaster ride in python 

#the program should ask the user to enter their age.
# Based on their age, provide different messages:
#if the user is between 18 and 45 years old (inclusive) ,  print("enjoy the ride!")
#if the user is under 18 years old, print ("you are too young for this ride")
#if the user is over 45 years old, print "You are too old for this ride."

print("To get access to the roller coaster ride")
age_checker = int(input("what is your age: "))

if age_checker >= 18 and age_checker <= 45:
    print("enjoy the ride")
elif age_checker < 18:
    print("You are too young for this ride")
elif age_checker > 45:
    print("you are too old for this ride")
else:
    print("check your age")             