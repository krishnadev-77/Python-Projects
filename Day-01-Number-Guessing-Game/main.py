"""
Project :- 1 
Number guessing game 

"""
import random

while True:


    secret_number = random.randint(1,100)

    guess = int(input("Guess a number between 1 to 100 :"))

    if guess == secret_number:
        print("🥳 Congratulations!! You guessed it right.. ")
    else:
        print("❌ Wrong! , The number was" , secret_number)