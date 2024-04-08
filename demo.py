#Get all the even numbers from 0 - 50

evens = []

for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)

evens = [number for number in range(50) if number % 2 == 0]
print(evens)        

#String that start with "a" and end in "y"

options = ["any", "albany", "apple","world", "hello", ""]
valid_strings = []

for string in options:
    if len(string) <= 1:
        continue
    
    if string[0]  != "a":
        continue
    
    if string[-1] != "y":
        continue
    
    valid_strings.append(string)

print(valid_strings)    

#Flattening a matrix (list of lists)
matrix = [ [1,2,3], [4,5,6],[7,8,9]]
flattened = []

for row in matrix:
    for num in row:
        flattened.append(num)


flattened = [num for row in matrix for num in row]
print(flattened)