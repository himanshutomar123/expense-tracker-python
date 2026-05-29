username="ht333939"
password=1234556
print("=========LOGIN SYSTEM =========")
attempts = 3

while attempts > 0:
    u=input("ENTER USERNAME:")

    if u == "stop":
            break
    p=input("ENTER PASSWORD:")

    if u == username and p == password:
        print("LOGIN SUCCESSFULLY")

    elif u !=username and p!=password:
        print("THE USERNAME AND PASSWORD ARE BOTH INCORRECT")

    else:
        attempts-=1
        print("TOTAL ATTEMPTS:",attempts)
        print("THANKS FOR USING PASSWORD APP")
if attempts == 0:
     print("ACCOUNT LOCKED")


    