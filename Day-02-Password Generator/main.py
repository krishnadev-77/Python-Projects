"""
Project :- 2 
Password Generator
"""

import random
import string

while True:
    length = int(input("Enter the length of the password :-"))


    letters = string.ascii_lowercase
    letters2 = string.ascii_uppercase
    num = string.digits
    special_characters = string.punctuation

    characters = letters2+letters+special_characters+num


    if length <= 0:
        print("Invalid input")
    else :
        password = ""

        for _ in range(length):
            password += random.choice(characters)

        print("Password Generated : " , password)

    choose = input("Do you want to generate another password (yes/no) :").lower()

    if choose == "no":
        print("Thanks for choosing password generator!!")
        break

    elif choose == "yes":
        continue
    
    else:
        print("Invalid input . Exiting...")
        break 
