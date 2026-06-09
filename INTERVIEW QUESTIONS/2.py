a = None
if a is None:
    print("a is None")

# Question: Reverse a string without using slicing ([::-1]).
string="python"
reverse=""
for ch in string:    
    reverse=ch+reverse
print(reverse)

num=1234
reverse_num=0
while num>0:
    last_digit=num%10 #4321
    reverse_num=reverse_num*10+last_digit
    num=num//10
    print(reverse_num)

# Question: Check if a string is a palindrome.

text="madam"
if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")
