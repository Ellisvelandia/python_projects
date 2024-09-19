questions = ( "How many are in a baker's dozen?", 
             "What is the capital of France?", 
             "What is the largest planet in our solar system?", 
             "What is the chemical symbol for gold?", 
             "Who is the main character in the book 'To Kill a Mockingbird'?" )

options = (
    ("A) 12", "B) 13", "C) 14", "D) 15"),
    ("A) Berlin", "B) Paris", "C) London", "D) Madrid"),
    ("A) Earth", "B) Saturn", "C) Jupiter", "D) Uranus"),
    ("A) Ag", "B) Au", "C) Hg", "D) Pb"),
    ("A) Scout Finch", "B) Huckleberry Finn", "C) Holden Caulfield", "D) Sherlock Holmes"),
           )

answers = ( "B", "B", "C", "B", "A" )
guesses = []
score = 0
questios_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[questios_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[questios_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is: {answers[questios_num]}")    
    questios_num += 1    
    

print("-----------------")    
print("      Results    ")    
print("-----------------")    


print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()    

print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()   

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")