# SIMPLE CALCULATOR USING IF ELSE:
num1 =int(input("ENTER FIRST NUMBER="))
num2 = int(input("ENTER SECOND NUMBER="))
op = input("ENTER OPERATOR(+ - * /):")
if op =="+":
    print(num1 + num2)
elif op == "-":
    print(num1-num2)
elif op =="*":
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")
