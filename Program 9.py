#PYTHON PROGRAM TO FIND THE LARGEST AMONG THREE NUMBERS:-
num1= int(input("ENTER THE FIRST NUMBER ="))
num2= int(input("ENTER THE SECOND NUMBER="))
num3= int(input("ENTER THE THIRD NUMBER ="))
if num1>num2 and num1>num3:
    print("The given number is largest among these:",num1)

elif num2>num1 and num2>num3:
    print("Largest=",num2)
    
else:
    print("Smallest")