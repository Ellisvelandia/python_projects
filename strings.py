# pets  = "Cats & Dogs"
# pets.index("&")
# print(pets.index("s"))

# def replace_domain(email, old_domain, new_domain):
#     if "@" + old_domain in email:
#         index = email.index("@" + old_domain)
#         new_email = email[:index] + "@" + new_domain
#         return new_email
#     return email

# print(replace_domain("Mz2gj@example.com", "google.com", "bing.com"))

# answer = "yes"
# if answer.lower() == "yes":
#     print("User said yes")
    
# name = "Ellis"
# number = len(name) * 3
# print("Hello {}, your lucky number is {}".format(name, number))    

# print(f"Hello {name} your lucky number is {number}")

# price = 7.5
# with_tax = price * 1.09
# print(price , with_tax)
# print("Base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax))

# def to_celsius(x):
#     return (x - 32) * 5 / 9
# for x in range(0, 101, 10):
#     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# basket = [
#     ("Peaches", 3.0 , 2.99),
#     ("Pears", 5.0 , 1.66),
#     ("Plums", 2.5 , 3.99),
#           ]

# subtotal = 0.00
# for item in basket:
#     fruit , weight , unit_price = item
#     subtotal += (weight * unit_price)
    
# tax_rate = 0.06625
# tax_amt = subtotal * tax_rate
# total = subtotal + tax_amt

# print("Subtotal:   ${:10,.2f}".format(subtotal))    
# print("Sales tax:  ${:10,.2f}".format(tax_amt))    
# print("total:      ${:10,.2f}".format(total))    
    
def mirrored_string(string):
    forward =  ""
    backward = ""    
    for character in string:
        if character.isalpha():
            forward += character
            backward = character + backward  
    if forward.lower() == backward.lower():
        return True
    return False          

print(mirrored_string("12 noon"))
print(mirrored_string("was it a  car or cat i saw"))
print(mirrored_string("eve, Madam eve"))