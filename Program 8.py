#Programs to check leaf year:-
year = int(input("ENTER THE YEAR YOU WANT TO CHECK ="))
if year%4==0 and year%100==0 and year%400==0:
    print("The given year is leaf year")
else:
    print("not a leaf year")