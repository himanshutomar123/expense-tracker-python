# Count the number of digits in a number:
number = 664
total = 0
for i in str(number):
        total +=1
print(total)

# Reverse a number:
num = 123
reverse = 0

while number > 0:
        digit = number % 10
        reverse = reverse * 10 +digit
        number// 10
print(reverse)