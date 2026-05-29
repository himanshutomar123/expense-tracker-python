# ========================================================= TRIANGLE PATTERNS ====================================================================
num = 7
for i in range(num):
    print(" " * (num-i-1),"*" *(2*i-1))


password = "him44283"

attempts = 3

while attempts > 0:
    user = input("ENTER PASSWORD: ")

    if user == "stop":
        print("THANKS FOR USING THIS APP")
        break

    elif user == password:
        print("THE PASSWORD IS CORRECT")
        break

    else:
        attempts -= 1
        print("THE PASSWORD IS NOT MATCH")
        print("ATTEMPTS REMAINS:", attempts)

if attempts == 0:
    print("NO ATTEMPTS LEFT")    
