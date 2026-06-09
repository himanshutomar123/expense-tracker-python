
year = int(input("ENTER YEAR TO CHECK WHETHER A LEAF YEAR OR NOT:"))
def leaf_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        return True
    else:
        return False

if leaf_year(year):
    print("YES,IT'S A LEAF YEAR")
else:
    print("NOT A LEAF YEAR")

