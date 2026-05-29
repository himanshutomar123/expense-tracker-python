num = [2, 3, 4, 5]
total = 0

for i in num:
    total += i

print(total)

num = [2, 5, 8, 11, 14, 17]
odd = 0
for i in num:
    print(i)
    if i % 2 != 0:
        odd +=1

print(odd)

num = [2, 5, 8, 11, 14, 17]
total = 0
for i in num:
    if i%2!=0:
        total +=i
print(total)

num = [3, 8, 1, 6, 9, 2, 10]
largest_even = 0
for i in num:
    if i %2 ==0:
        if largest_even is None or i > largest_even:
            largest_even =i
    
print(largest_even)
        
num = [2, 5, 8, 11, 14, 17]
total_even = 0
total_odd = 0
for i in num:
    if i %2 ==0:
        total_even +=1
    else:
        total_odd +=1
print(total_even)
print(total_odd)

num = [2, 5, 8, 11, 14, 17]
total_even = 0
total_odd = 0
for i in num:
    if i % 2 ==0:
        total_even +=i
    else:
        total_odd +=i

print(total_even)
print(total_odd)