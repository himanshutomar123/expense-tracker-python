#----------------------------------------------- CALCULATOR(Using Functions)-----------------------------------------------------------------------
print("===== WELCOME TO MY CALCULATOR ====")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return(a*b)

def div(a,b):
    if b==0:
        return "can't divide by zero"
    return a/b
result=add(55,22)
result2=sub(44,3)
result3=sub(55,3)
result4=mul(33,3)

print("Add:", result)
print("Sub:", result2)
print("Mul:", result3)
print("Div:", result4)

while True:

    print("\n------ MENU ------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice=input("ENTER YOUR CHOICE:")
    if choice == "5":
        print("Thanks for using our calculator")
        break
    else:
        print("Invalid")

    if choice in ["1","2","3","4"]:
        num1=float(input("ENTER FIRST NUMBER:"))
        num2=float(input("ENTER SECOND NUMBER:"))

        if choice =="1":
            print("Result =",add(num1,num2))
        
        elif choice =="2":
            print("Result =",sub(num1,num2))

        elif choice =="3":
            print("Result =",mul(num1,num2))
        
        elif choice =="4":
            print("Result =",div(num1,num2))
    
    else:
        print("Invalid Choice")

    






