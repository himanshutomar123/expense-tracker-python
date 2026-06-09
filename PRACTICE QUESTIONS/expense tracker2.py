expenses=[]

def add_expense():
    date = input("Enter The Date: ")
    category = input("Enter Type (Food, Travel, Books): ")
    description = input("Enter More Details (What you ate / Where you traveled): ")
    amount = float(input("Total Amount You Spent: "))

    expense={
        'date':date,
        'category':category,
        'description':description,
        'amount':amount
    }

    expenses.append(expense)
    print("YOUR EXPENSES ADDED SUCCESSFULLY")

def view_expense():
    if len(expenses)== 0:
        print("NO EXPENSES FOUND")
    else:
            print("\n====== ALL EXPENSES ======")

    for i, expense in enumerate(expenses, start=1):
            print(f"\nExpense #{i}")
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Amount: ₹{expense['amount']}")

def view_total():
      
      total=0

    for item in expenses:
         otal += item["amount"]

    print("\nTOTAL SPENT =", total)



    

