#  Reverse a number:-
num = 123
reverse = int(str(num)[::-1])
print(reverse)

alpha = "tomar"
reverse = str(alpha)[::-1]
print(reverse)

# Keep asking the user for a password until they enter the correct one:-
password = 1234
while True:
    num = int(input("ENTER THE CORRECT PAWWORD:"))
    if num == password:
        print("correct password")
        break

# Print all elements in a list of fruits:
a = ["apple", "banana", "mango"]
print(a)

num = 5
while num>0:
    print(num)
    num-=1