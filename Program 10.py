#CHECK IF A NUMBER IS PRIME OR NOT:- 
num = int(input("ENTER THE NUMBER ="))

if num==1:
    print("It's not a prime number")

if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
            break
        else:
            print("It's a prime number")

    