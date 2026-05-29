'''
                                                    STUDENT MARKS MANAGER:-
CREATE A PROGRAM THAT:
    1.ASK HOW MANY STUDENTS
    2.TAKE STUDENTS NAME
    3.TAKE MARKS
    4.STORE DATA
    5.AFTER INPUT,
    **SHOW:
.ALL STUDENTS
.AVERAGE MARKS
.HIGHEST SCORER
.LOWEST SCORER
.PASS/FAIL(PASS>=40)

# NOW WHAT I HAVE TO DO :-
1.FIRST MAKE VARABLE TO STORE STUDENTS,MARKS,HIGHEST,LOWEST,
2.TAKE HOW MANY STUDENTS ARE IN
3.TAKE STUDENTS NAME
4.TAKE MARKS
5.

'''
n=int(input("ENTER NUMBER YOU WANT TO CHECK IT'S A PRIME OR NOT:"))


i=2             #i is the starting divisor and Prime checking begins from 2 because 1 is not used to test prime numbers.
flag=0           #flag is used to track whether the number is divisible.
                # 0 means:
                # “No divisor found yet.” Later, if a divisor is found, flag becomes 1.

if n<2:
    print("NOT A PRIME NUMBER")
else: 
    while n>i:
        if n%i==0:
            flag=1
            break
        i=i+1
    if flag==1:
        print("NOT A PRIME NUMBER")
    else:
        print("YES,IT'S A PRIME NUMBER")


  




