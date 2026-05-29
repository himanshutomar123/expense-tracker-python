num = 88
if num<=1:
    print("Not Prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not Prime")
            break 
        else:
            print("Prime")

# Print all prime numbers between 1 and 100:
for num in range(2, 101):

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)