import sqlite3

# Database Connection
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT
)
""")

conn.commit()


def add_expense():
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")
    date = input("Enter Date (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO expenses(amount, category, date) VALUES (?, ?, ?)",
        (amount, category, date)
    )

    conn.commit()
    print("Expense Added Successfully!")


def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if not expenses:
        print("No Expenses Found!")
        return

    print("\nID\tAmount\tCategory\tDate")
    print("-" * 40)

    for expense in expenses:
        print(f"{expense[0]}\t{expense[1]}\t{expense[2]}\t{expense[3]}")


def delete_expense():
    expense_id = int(input("Enter Expense ID to Delete: "))

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Expense Deleted Successfully!")
    else:
        print("Expense ID Not Found!")


def monthly_report():
    month = input("Enter Month (YYYY-MM): ")

    cursor.execute("""
    SELECT SUM(amount)
    FROM expenses
    WHERE substr(date,1,7)=?
    """, (month,))

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"Total Expenses for {month}: ₹{total}")


def category_report():
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    data = cursor.fetchall()

    if not data:
        print("No Expenses Found!")
        return

    print("\nCategory Report")
    print("-" * 25)

    for category, total in data:
        print(f"{category}: ₹{total}")


# Main Menu
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Monthly Report")
    print("5. Category Report")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        monthly_report()

    elif choice == "5":
        category_report()

    elif choice == "6":
        print("Thank You For Using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Try Again.")

conn.close()