while True:
    num1 = float(input("ENTER FIRST NUMBER:"))
    operator=input("ENTER OPERATOR(+ - * /):")
    num2 = float(input("ENTER SECOND NUMBER:"))
    if operator=='+':
        print(num1+num2)
    elif operator=='-':
        print(num1-num2)
    elif operator=='*':
        print(num1*num2)
    elif operator=='/':
        print(num1/num2)
    else:
        print("invalid operator")
    choice = input("condition? (y/n):")
    if choice == "n":
        break
    