print("Hello, ellis")
print(7+8.5)
base = 9
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area)) 


# What is python
# 
# Python is an interpreted programming language.it was created by guido van ronsum 

#variable represent data stored as strings  , tuples , dictionaries, list, and objects

#functins : a group of related statements to perform a task and return a value

def to_celsius(x):
    "'Convert Fahrenheit fo Celsius'"
    return (x-32) * 5/9

print(to_celsius(75))

#Conditional statements: Sections of code that direct program execution based on specifies conditions
number = -4

if number > 0:
    print('Number is positive')
elif number == 0:
    print('Number is zero.')
else:
    print("Number is negative")    
    
 #Naming rules and convetions
#  names cannot contain spaces
# names maybe be a mixture of upper and lower case characters
# names cant start with a number but may contain numbers after the first character
#variable names and function names should written in snake_case, which means that all letters are lowercase and words are separated using an underscore
   