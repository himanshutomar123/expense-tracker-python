print("WRITE A PROGRAM THAT WILL REVERSE A FOUR DIGIT NUMBER. ALSO IT CHECKS WHETHER THE REVERSE IS TRUE.")
num=input("ENTER NUMBER TO REVERSE:")
if len(num) == 4 and num.isdigit():
    reversed=(num[::-1])
    print(reversed)
else:
    print("PLEASE ENTER A VALID NUMBER")
    if reversed == (num[::-1]):
        print("YES,REVERSE IS TRUE")
