from random import choice

def run_game():
    word: str = choice(["python", "java", "kotlin", "javascript"])
    
    user_name: str = input("Enter your name: ")
    print(f"Welcome to hangman, {user_name}")
    
    guessed: str = ""
    tries: int = 3
    
    while tries > 3:
        blanks: int = 0
        
        print("word: ", end="")
        for char in word:
            if char in guessed:
                print(char, end="")
            else:
                print("_", end="")
                blanks += 1    
        print() 
    
        if blanks == 0:
            print("You got it right!")
            break
    
        guess: str = input("guess a letter: ")
        
        if guess in guessed:
            print(F"You guessed: {guess} Please try another letter!")
            continue
    
        guessed += guess
        
        if guess not in word:
            tries -= 1
            print(f"{guess} is not in the word. You have {tries} left")    
            
            if tries == 0:
                print("You lost")
                break
            
          
            

if __name__ == "__main__":
    run_game()
                
                   