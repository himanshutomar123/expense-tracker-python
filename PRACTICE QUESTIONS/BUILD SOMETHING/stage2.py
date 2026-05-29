# NUMBER GUESSING GAME:-
import random

num=random.randint(1,5)
for i in range(5):
    print("GUESS NUMBER BETWEEEN 1 TO 5")
guess=int(input("ENTER GUESS NUMBER="))

if guess==num:
    print("YOU GUESSED CORRECT:",guess)
elif guess > num:
    print("GUESS IS HIGH")
else:
    print("GUESS IS LOW")
    print("THE CORRECT NUMBER WAS:",num)


# PASSWORD CHECKER:-
password="lesnar#$55ee"
for i in range(3):
    checker = input("ENTER THE CORRECT PASSWORD:")

    if checker == password:
        print("ACCESS GRANTED")
        break
        
    else:
        print("WRONG PASSWORD")
        print("Attempts left:", 2 - i)



