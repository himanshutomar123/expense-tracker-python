num = [3, 7, 2, 9, 5]
Largest = num[0]
for i in num:
    if i>Largest:
        Largest = i

print(Largest)


num = [3, 7, 2, 9, 5]
largest = num[0]
second_largest = num[0]
for i in num:
    if i > largest:
      second_largest = largest 
      largest = i
    elif i> second_largest and  i!=largest:
       second_largest = i

print(second_largest)


num = [2,3,4,5,6,7,8,44]
smallest = num[0]
for i in num:
   if i<smallest:
      smallest = i
print(smallest)


num = [2,3,4,5,6,7,8,44]

smallest = float('inf')
second_smallest = float('inf')

for i in num:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    elif i < second_smallest and i != smallest:
        second_smallest = i

print(second_smallest)