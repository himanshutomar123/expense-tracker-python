# Count how many numbers from 1 to 100 are divisible by 5:-
count = 0
for i in range(1,100):
    if i % 5 == 0:
        print(i)
        count +=1
print(count)

# Count how many numbers from 1 to 200 are divisible by both 3 and 5:-
count = 0
for i in range(1,201):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        count +=1
print("THE TOTAL NUMBER IS DIVISIBLE BY 3 AND 5 IS:",count)



#Count numbers from 1 to 300 divisible by 2 AND 7:-
count = 0
for i in range(1,301):
    if i % 2 == 0 and i % 7 == 0:
        print(i)
        count +=1
print("TOTAL",count)

# Print numbers from 1 to 100 that are:

# divisible by 3 OR 5, but NOT both at the same time:-
count = 0 
for i in range(1,101):
    if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0):
        print(i)
        count +=1
print("TOTAL",count)

# Print numbers from 1 to 200 that are:

# divisible by 4 OR 6
# BUT NOT both:-
count = 0
for i in range(1,201):
    if (i % 4 == 0 or i % 6 == 0) and not (i % 4 == 0 and i % 6 == 0):
        print(i)
        count += 1
print("TOTAL",count)

''' 👉 Print numbers from 1 to 300 that are:

divisible by 2 OR 3 OR 5
BUT NOT divisible by 6'''

count = 0
for i in range(1,301):
    if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0) and not i % 6 != 0:
        print(i)
        count +=1
print("TOTAL",count)


'''
Print numbers from 1 to 300 that are:

divisible by 2 OR 3 OR 5
BUT NOT divisible by 2 AND 3 together
'''
count = 0
for i in range(1,301):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 and not i % 2 == 0 and i % 2 == 0:
        print(i)
        count += 1
print("TOTAL",count)


# Check if a number is positive, negative, or zero:-
num = 55
if num > 0 :
    print("Postive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Find the largest of 2 numbers:-
num1 = 44
num2 = 66
if num2 > num1 :
    print("largest")
else: 
    print("not largest")
