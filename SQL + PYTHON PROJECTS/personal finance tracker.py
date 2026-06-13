transactions = []

while True:
    print("\n===== Finance Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))

        transaction = {
            "type": "income",
            "amount": amount
        }

        transactions.append(transaction)
        print("Income added successfully!")

    elif choice == 2:
        amount = float(input("Enter expense amount: "))
        category = input("Category: ")

        transaction = {
            "type": "expense",
            "amount": amount,
            "category": category
        }

        transactions.append(transaction)
        print("Expense added successfully!")

    elif choice == 3:
        if not transactions:
            print("No transactions found.")
        else:
            for t in transactions:
                print(t)

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")