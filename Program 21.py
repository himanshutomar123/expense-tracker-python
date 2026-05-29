# Find the largest even number AND smallest odd number in one loop
num = [12, 7, 4, 19, 8, 3, 15, 10]
largest_even = None
smallest_odd = None
for i in num:
    if i % 2 == 0:
        if largest_even is None or i>largest_even:
            largest_even =i
    else:
        if smallest_odd is None or i<smallest_odd:
            smallest_odd = i

print(largest_even)
print(smallest_odd)

# Problem: Difference Between Largest and Smallest
num = [8, 3, 15, 1, 9]
largest = None
smallest = None
for i in num:
    if largest is None or i > largest:
        largest = i
    else:
        if smallest is None or i < smallest:
            smallest = i
print(largest)
print(smallest)
Difference = largest - smallest
print(Difference)

# Find difference between largest even and smallest odd

num = [14, 3, 9, 20, 7, 6, 11, 2]
largest_even = None
smallest_odd = None
for i in num:
    if i % 2 == 0:
        if largest_even is None or i > largest_even:
            largest_even = i
    else:
        if smallest_odd is None or i < smallest_odd:
            smallest_odd = i
print(largest_even)
print(smallest_odd)
Difference = largest_even - smallest_odd
print(Difference)

print(max(44,33))