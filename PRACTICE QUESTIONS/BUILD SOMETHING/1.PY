'''
Project 1: Number guessing game
computer picks a number
user guesses
hints: “too high / too low”
'''
import random

secret_number = random . randint (1,11)

print("GUESS THE NUMBER BETWEEN  1 TO 11 ")

guess=int(input("ENTER YOUR GUESS:"))

if guess==secret_number:
    print("YOUR GUESS IS CORRECT:")
else:
    print("WORNG GUESS")
    print("THE RANDOM NUMBER WAS :",secret_number)




    
