def greeting(name):
    print("welcome, " + name)

greeting("Kay")    
greeting("Cameron")    

def greetings(name , deparment):
    print("Welcome, " + name)
    print("You are part of " + deparment)

greetings("Blake", "Software engineering")    
greetings("Ellis", "Software engineering")    

month = "September"
print(f"I investigated failed login attempts during", month)

print(type("This is a string"))

number = 12
string_representation = str(number)
print(string_representation)

time_list = [12,2,21,32,19,57,22,14]
print(sorted(time_list))
print(min(time_list))
print(max(time_list))

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a  + area_b
print("The sum of the boths areas is: " + str(sum))



def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

name = "Ellis"
number = len(name) * 9 

print(F"Hello {name} your lucky number is {number}")

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + " Your lucky number is " + str(number))


lucky_number("Crisanto")
lucky_number("Caicedo")

def calculate(d):
    q = 3.14
    z = q * (d ** 2 )
    print(z)
    
calculate(5)    

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)    