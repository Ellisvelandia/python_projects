# # message = "Hello world"
# # print(message)

# # greetings = "Ellis is awesome"
# # print(greetings)

# # game_score = 2
# # health = 87.5
# # game_on = True

# # print(game_score , health , game_on)

# # name = input("What is your name? ").title()
# # print(name)

# # price = 10

# # print(not price > 10)

# # user = input("Ente your name: ").title()

# # if user == "Ellis":
# #     print("Welcome back " + user)
# # elif user == "Crisanto":
# #     print("Welcome back " + user)    
# # else:
# #     print("User doesn't exist")    

# #Your task is to create a simple age checker for a roller coaster ride in python 

# #the program should ask the user to enter their age.
# # Based on their age, provide different messages:
# #if the user is between 18 and 45 years old (inclusive) ,  print("enjoy the ride!")
# #if the user is under 18 years old, print ("you are too young for this ride")
# #if the user is over 45 years old, print "You are too old for this ride."

# # print("To get access to the roller coaster ride")
# # age_checker = int(input("what is your age: "))

# # if age_checker >= 18 and age_checker <= 45:
# #     print("enjoy the ride")
# # elif age_checker < 18:
# #     print("You are too young for this ride")
# # elif age_checker > 45:
# #     print("you are too old for this ride")
# # else:
# #     print("check your age")             

# # count = 1

# # while count <= 5:
# #     print(count)
    
# #     user_input = input("Enter 'exit' to end ")
    
# #     if user_input.lower() == 'exit':
# #         print("Exiting the program. goodbye")
# #         break
# #     else:
# #         print("What do you mean? ")    
    
# #     count += count 

# # names = ["Luna", "Emma", "Karl", "Noah"]
# # names[0] = "Ellis" 
# # names.append("Ava")
# # names.pop()
# # print(names)

# # numbers = [1,2,3,4,5]
# # new_numbers = []

# # for item in numbers:
# #     print(item)
    
    
# #     new_numbers.append(item + 1)    
# # print(new_numbers)    

# # customer = {
# #     "id": 101,
# #     "name": "Ellis",
# #     "phone": "555-1234",
# #     "premium_member": True
# # }

# # print(customer)
# # print(customer["id"])

# customers = [
#     {
#     "id": 101,
#     "name": "Ellis",
#     "phone": "555-1234",
#     "premium_member": True 
#     },
#     {
#      "id": 102,
#     "name": "crisanto",
#     "phone": "54444-222",
#     "premium_member": False
#     }
# ]

# for customer in customers:
#     print(customer["id"])
#     print(customer["name"])
#     print(customer["phone"])
#     print(customer["premium_member"])

# tuple
# numbers = (1,2,3)
# print(numbers[0])
# print()
# input()

# def greet():
#   print("Welcome back ellis")
  

# greet()  

# def greet(name):
#     print("Welcome back " + name)

# greet("Ellis")    

#this is a Note/comment
# first_name = "Ellis"
# last_name = "Velandia"
# print("Hello there everyone learning! " + "My name is " + first_name + " and my last name is " + last_name)

num_list = [1,2,3,4,5]
total = 0

for number in num_list:
    total += number
average = total / len(num_list)
print(average)     