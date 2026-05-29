# Find factorial of a number:-
num = int(input("ENTER NUMBER="))
fact= 1
for i in range(1,num + 1):
    fact = fact * i
print("FACTORIAL:",fact)

num = 5
fact = 1
total = 0
for i in range(1,num+1):
    fact = fact * i
    total = total + fact 
print(fact)
print(total)