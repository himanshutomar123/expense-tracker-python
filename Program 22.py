# 🔥 Problem: Count Numbers Greater Than Average
# 👉 Question:


num = [4, 8, 6, 10, 2]

total = 0

for i in num:
    total += i
    

average = total / len(num)
                  

count = 0

for i in num:
    if i > average:
        count += 1
        break

print(count)


# Runs until user types "exit":-
type = "exist"
while True:
    str = input("ENTER CORRECT:")
    if str == type:
        print("ok")
        break

# You loop through each character in a string:-
str = "Himanshu Tomar"
for i in str:
    print(i)