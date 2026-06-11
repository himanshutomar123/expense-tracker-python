import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT
)
""")
conn.commit()

# Functions
def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    date = date_entry.get()

    if not amount or not category or not date:
        messagebox.showerror("Error", "Fill all fields")
        return

    cursor.execute(
        "INSERT INTO expenses(amount, category, date) VALUES (?, ?, ?)",
        (amount, category, date)
    )
    conn.commit()

    load_data()

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def load_data():
    tree.delete(*tree.get_children())

    cursor.execute("SELECT * FROM expenses")

    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)

def delete_expense():
    selected = tree.selection()

    if not selected:
        return

    item = tree.item(selected[0])
    expense_id = item["values"][0]

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )
    conn.commit()

    load_data()

# GUI
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("800x500")

tk.Label(root, text="Amount").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=2, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=3, column=0)
tk.Button(root, text="Delete Selected", command=delete_expense).grid(row=3, column=1)

tree = ttk.Treeview(
    root,
    columns=("ID", "Amount", "Category", "Date"),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Amount", text="Amount")
tree.heading("Category", text="Category")
tree.heading("Date", text="Date")

tree.grid(row=4, column=0, columnspan=4, padx=10, pady=20)

load_data()

root.mainloop()

conn.close()
'''
o build a real desktop expense tracker app yourself (without copying code), focus on learning these topics in order:

1. Python Fundamentals (Must Know)

You should be comfortable with:

Variables
Data types
Lists, tuples, dictionaries
Loops (for, while)
Conditions (if, elif, else)
Functions
Modules

Example:

def add_expense(amount):
    print(amount)
2. Object-Oriented Programming (OOP)

Most real apps use classes.

Learn:

Classes
Objects
Constructors (__init__)
Methods

Example:

class Expense:
    def __init__(self, amount, category):
        self.amount = amount
        self.category = category

Difficulty: ★★★☆☆

3. File Handling

Before databases, learn:

with open("data.txt", "a") as file:
    file.write("Food,200\n")

Learn:

Read files
Write files
CSV files

Difficulty: ★★☆☆☆

4. SQLite Database

This is the biggest step toward real applications.

Learn:

Create database
Create tables
Insert data
Update data
Delete data
Select data

Example:

import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

Difficulty: ★★★☆☆

5. GUI Development (Tkinter)

This turns your program into a real app.

Learn:

Windows
Buttons
Labels
Entry boxes
Tables (Treeview)
Frames

Example:

import tkinter as tk

root = tk.Tk()
root.mainloop()

Difficulty: ★★★☆☆

6. Error Handling

Real apps shouldn't crash.

Learn:

try:
    amount = float(input())
except ValueError:
    print("Invalid number")

Difficulty: ★★☆☆☆

7. Date & Time
from datetime import datetime

today = datetime.now()

Useful for:

Expense dates
Reports
Monthly summaries

Difficulty: ★★☆☆☆

8. Data Visualization

Learn matplotlib.

Example:

import matplotlib.pyplot as plt

Use it for:

Pie charts
Expense reports
Monthly trends

Difficulty: ★★★☆☆

9. Project Structure

Instead of one huge file:

expense_tracker/
│
├── main.py
├── database.py
├── gui.py
├── reports.py
├── utils.py
└── expenses.db

This is how professional projects are organized.

Difficulty: ★★★☆☆

10. Git & GitHub

Learn:

git init
git add .
git commit -m "Initial Commit"

Store projects on GitHub and build a portfolio.

Difficulty: ★★★☆☆

Recommended Learning Path
Python Basics ✓
Functions ✓
OOP
File Handling
'''