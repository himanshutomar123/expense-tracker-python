
expenses=[]
print("=" * 50)
print("WELCOME TO EXPENSE TRACKER")
print("1. Add Expense")
print("2. View Expenses")
print("3. Delete Expense")
print("4. Exit")

while True:

    choice=int(input("ENTER YOUR CHOICE="))
    
    if choice == 1:
        amount=float(input("ENTER YOUR AMOUNT:"))
        category=input("ENTER ITEM CATEGORY:")
        date=(input("ENTER DATE :"))
        description=input("ENTER DESCRIPTION:")

        expense={
            "amount":amount,
            "category":category,
            "date":date,
            "description":description
        }

        expenses.append(expense)
        print("\n Your Expenses Added Successfully")

    elif choice ==2:
        if len(expenses)==0:
            print("No Expenses Found")
        else:
            print("============EXPENSES LIST==========")
            for i in expenses:
                print(i)
    
    elif choice == 3:
        if len(expenses) == 0:
            print("No Expenses Found")
    else:
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. {expense}")

        delete_expense = input("ENTER CATEGORY TO DELETE: ")
        found = False

        for i in expenses:
            if i["category"].lower() == delete_expense.lower():
                expenses.remove(i)
                found = True
                print("Expense Deleted Successfully")
                break

        if not found:
            print("Expense Not Found")

        elif choice == 4:
            print("Thanks for using this Expense App")
        break




    

