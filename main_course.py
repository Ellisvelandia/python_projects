# # greeting = "Hello world"
# # for char in greeting:
# #     print(char)

# # greeting = "Hello world"
# # for i in range(len(greeting)): 
# #     print(i)

# # greeting = "Hello world"
# # index =  0
# # while index < len(greeting):
# #     print(greeting[index])
# #     index += 1

# # greeting = "Hello world"
# # index =  0
# # while index < len(greeting):
# #     print(greeting[index: index + 1])
# #     index += 1
    
# # numbers =[1,2,3,4,5]
# # squared_numbers = [x ** 2 for x in numbers] 
# # print(squared_numbers)   

# def c_to_f(temp):
#     return (temp * 9 / 5) + 32
    
# celsis_temps = [0.0, 10.0, 20.0, 30.0,40.0,50.0]

# fahrenheit_temps = list(map(c_to_f, celsis_temps)
# )

# print(fahrenheit_temps)
# # for temp in fahrenheit_temps:
# #     print(temp)

# greetings = ["Hello", "World"]
# print(" ".join(greetings))
# name = "Ellis"
# print("Hello, " + name + "!")

# def greet_friends(friends):
#     for friend in friends:
#         print("Hello, " + friend + "!")

# greet_friends(["Ellis", "Crisanto", "Maria", "Elsa"])

# for n in range(19):
#     if n % 2 == 0:
#         print(n)

# input = "Four score and seven years ago"
# for c in input:
#   if c.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(c)
# print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])
# print(input.count("aeiou"))

# for c in range(len(input)):
#   if c in ['a', 'e', 'i', 'o', 'u']:
#     print(c)

# def sum_positive_numbers(n):
#     # The base case is when n is 1 or less
#     if n < 1:
#         return 0

#     # The recursive case is adding this number to 
#     # the sum of the numbers smaller than this one.
#     return n + sum_positive_numbers(n - 1)

# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15


# def factorial(n):
#     if n < 2:
#         return 1
#     return n * factorial(n - 1)


# factorial(5)
    
# def recursive_function(parameters):
#     if base_case_condition:
#         return base_case_value
#     recursive_function(update_parameters)