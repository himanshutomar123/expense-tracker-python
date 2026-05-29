from array import *
sum=0
multiply=1
largest=None
smallest=None
second_largest=None
second_smallest=None
even_count=0
odd_count=0

a=array('i',[1,2,3,5,6,4,33])
print(a)
print(max(a))
print(min(a))
print(len(a))
a.reverse()
print(a)
 # NOW REVERSING ARRAY WITHOUT USING REVERSE():


reversed_array = array('i', [])

for i in range(len(a)-1, -1, -1):
    reversed_array.append(a[i])

print("Reversed Array:", reversed_array)

for i in a:
# EVEN COUNT:
    if i % 2==0:
        print("even")
        even_count+=1
        # ODD COUNT
    if i % 2!=0:
        print("odd")
        odd_count+=1

     # Largest and second largest
    if largest is None or i>largest:
        second_largest = largest
        largest = i
    
          
    elif second_largest is None or i > second_smallest:
        second_largest=i
    sum+=i
    multiply*=i

# Smallest and second smallest
    if smallest is None or i < smallest:
        second_smallest = smallest
        smallest = i

    elif second_smallest is None or i < second_smallest:
        second_smallest = i

average=sum/len(a)
print("SUM:",sum)
print("MULTIPLY:",multiply)
print("AVERAGE:",average)
print("Largest:", largest)
print("Second Largest:", second_largest)
print("smallest:",smallest)
print("second_smallest:",second_smallest)
print("Count even:",even_count)
print("odd count:",odd_count)

a=array('i',[1,2,3,5,6,4,33])
new_array=a.remove()
print(new_array)
    

