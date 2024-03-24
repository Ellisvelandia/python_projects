print("Welcome to the simple ATM simulator")

balance = 1000
user_pin = "1234"
entered_pin = input("Please enter your PIN ")

if entered_pin != user_pin:
    print("Invalid PIN. Exiting")
    atm_on = False
else:
    # print("success PIN")
    atm_on = True        
    
while atm_on:
    print("Main Menu:")
    print("1. Check balance")    
    print("2. Deposit Money")    
    print("3. Withdraw Money")    
    print("4. Exit")    
    
    choice = input("Enter your Choice: ")
    
    if choice == "1":
       print("Your current balance is $" + str(balance))
    
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: $"))
        balance += amount
        print("$" + str(amount) + " deposited succssfully")   
    
    elif choice == "3":
        amount =  float(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print("Insufficiente balance!")
        else:
            balance -= amount
            print("$" + str(amount) + " Withdraw successfully")         
    
    elif choice == "4":
        print("Thank you for using our service ATM")
        atm_on = False
    
    else:
        print("Invalid choice. Please try again")              