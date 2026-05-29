# Check if a number is prime:
num = int(input("ENTER NUMBER ="))
if num <= 1:
    print("not a prime")
else:
    for i in range (2,num):
        if num % i == 0:
            print("not prime")
            break
        else:
            print("prime")