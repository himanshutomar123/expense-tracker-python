# Q:1 PRINT ALL NUMBERS FROM 1 TO 10 USING WHILE LOOP:
i = 0
while i < 11:
    print(i)
    i+=1

i = 0
while i<122:
    print(i)
    i+=1

# Q:2 PRINT NUMBERS FORM 10 DOWN TO 1 REVERSE ORDER:-
i = 10
while i>=1:
    print(i)
    i-=1
    
# Q:3 PRINT ALL EVEN NUMBERS BETWEEN 1 TO 100:
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# Q:4 PRINT ALL ODD NUMBERS BETWEEN 1 TO 100:
i = 1
while i<= 100:
    if i % 2 != 0:
        print(i)
    i+=1

# Q:5 PRINT MULTIFICATION TABLE OF A GIVEN  NUMBER FORM n x 1 to n x 10.
num = 3
i = 1
while i < 11:
    print(num,"x",i ,"=",num * i)
    i+=1

num = 44
i = 1
while i < 11:
    print(num,"x",i,"=",num * i)
    i +=1


num = 97
i = 1
while i < 11:
    print(num,"x",i,"=",num*i)
    i+=1

# Q:6 CALCULATE AND PRINT THE SUM OF ALL FIRST N NATURAL NUMBERS:
n = 5
i = 1
sum = 0
while i<=n:
    sum +=i       
    i+=1
print("sum",sum)

n = 66
i = 1
sum = 0
while i<=n:
    sum +=i
    i+=1
print("SUM OF FIRST 66 NATURAL NUMBER:",sum)


# Q7:- CALCULATE THE SUM  OF ALL EVEN  NUMBERS FROM 1 TO 100:
i = 1
sum_even= 0
while i<=100:
    if i % 2 == 0:
        print(i)
        sum_even +=i
    i+=1
print("SUM OF ALL EVEN NUMBERS FROM 1 TO 100 :",sum_even)
        
# Q8:- CALCULATE THE SUM OF ALL ODD NUMBERS FROM 1 T0 100:
i = 1
sum_odd = 0
while i<=100:
    if i % 2 !=0:
        print(i)
        sum_odd+=i
    
    i+=1
print("SUM OF ALL ODD NUMBERS FROM 1 TO 100:",sum_odd)

# Q:9 CALCULATE AND PRINT THE FACTORIAL OF THE GIVEN NUMBER:
num = 5
i = 1
fact = 1
while i <= num:
    fact*=i
    i+=1
print("Factorial:",fact)

num = 8
i = 1
fact = 1
while i<= num:
    fact *= i
    i+=1
print("FACTORIAL:",fact)

# Q10:- FIND AND PRINT THE PRODUCT OF ALL DIGITS OF A GIVEN NUMBER:-
num = 7474
pro = 1

while num > 0:
    digit = num % 10
    pro *= digit
    num //= 10

print("Product of digits =", pro)


num = 123
sum = 1
while num>0:
    digit = num % 10
    sum += digit
    num//= 10
print("SUM OF DIGITS:",sum)

# Q:11 COUNT AND PRINT THE TOTAL NUMBER OF DIGITS OF A GIVEN NUMBERS:
num = 44332
total_digit = 0
while num > 0:
    total_digit +=1
    num//=10
print("COUNT:",total_digit)

# Q:12 REVERSE THE GIVEN NUMBER AND PRINT REVERSED VALUE:
num =123
i = 0
reversed = 0
while num>0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num //= 10

print("REVERSED NUMBER:",reversed)

num =843
i = 0
reversed = 0
while num>0:
    digit = num % 10
    reversed = reversed * 10 + digit
    num//= 10
print("REVERSED:",reversed)

# Q:13 CHECK WHETHER A NUMBER IS A PALINDROME:-
num = 121
temp = num
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

if num == reversed_num:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q:14 FIND AND PRINT THE  PRODUCT OF ALL DIGITS OF A GIVEN NUMBER:-
num = 232
pro = 1
while num>0:
    digit = num%10
    pro *= digit
    num//=10
print(pro)

num = 232
sum = 1
while num>0:
    digit = num % 10
    sum += digit
    num //=10
print(sum)

# Q:15 CHECK WHETHER A GIVEN NUMBER IS AN ARMSTRONG NUMBER:-
num = 153
temp = num
sum = 0
while temp>0:
    digit = temp % 10
    sum = sum +(digit * digit * digit)
    temp = temp//10

if sum == num:
    print("ARM STRONG")
else:
    print("not armstrong")

# THIS IS THE REASON WE USE TEMP INSTEAD OF NUM,BECAUSE NUM WOULD ZERO.
num = 153
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10   
print(num)
'''''
# 🔑 When to use temp = num
1. 🔢 Digit-based problems (MOST COMMON)

Whenever you do things like:

extract digits (% 10)
remove digits (// 10)

You will destroy the number, so you need a copy.

✅ Examples:

Armstrong number ✔
Palindrome number (e.g., 121)
Reverse a number (123 → 321)
Sum of digits (123 → 6) '''

# Q:16 CHECK WHETHER A GIVEN NUMBER IS PERFECT NUMBER:-

num = 6

sum = 0

# find divisors
for i in range(1, num):
    if num % i == 0:
        sum = sum + i

# check
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")

# Q:17 PRINT ALL PRIME NUMBERS BETWEEEN 1 TO 100.
num =7

if num <= 1:
    print("NOT A PRIME NUMBER")
else:
    for i in range(2,num):
        if num % i == 0:
            print("NOT A PRIME NUMBER")
            break 
    else:
        print("PRIME NUMBER")

    
num = 3333
if num<=1:
    print("Not a prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime number")
        
#Q:18 PRINT ALL PRIME NUMBERS BETWEEN 1 T0 100:
for num in range(2,101):
    for i in range(2,num):
        if num % i == 0:
            break
        else:
            print(num ,end="")

