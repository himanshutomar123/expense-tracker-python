while True:
    num1=float(input("ENTER THE FIRST NUMBER:"))
    num2=float(input("ENTER THE SECOND NUMBER:"))
    op=input("SELECT OPERATOR :(+,-,*,/)")

    if op == '+':
        print("Result:",num1+num2)

    elif op == '-':
        print("Result:",num1-num2)

    elif op == '*':
        print("Result:",num1*num2)

    elif op == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        print("Result:",num1/num2)
    else:
        print("INVALID OPERATOR!")

    print("THANKS FOR USING THIS CALCULATOR")
    choice = input("condition? (y/n):")

    if choice =="n":
     break
