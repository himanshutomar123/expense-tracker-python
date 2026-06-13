import sqlite3

print("-" * 50)
print("CONTACT BOOK USING SQLITE")
print("-" * 50)
print("-" * 50)

# Connect to database
conn = sqlite3.connect("contact.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
                    CREATE TABLE IF NOT EXISTS CONTACTS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone TEXT
)
""")
conn.commit()

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Add Contact
    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        cursor.execute(
            "INSERT INTO CONTACTS (name, phone) VALUES (?, ?)",
            (name, phone)
        )
        conn.commit()

        print("Contact Added Successfully!")

    # View Contacts
    elif choice == 2:
        cursor.execute("SELECT * FROM CONTACTS")
        contacts = cursor.fetchall()

        if not contacts:
            print("No contacts found.")
        else:
            print("\nContacts:")
            print("-" * 30)

            for contact in contacts:
                print(f"ID: {contact[0]}")
                print(f"Name: {contact[1]}")
                print(f"Phone: {contact[2]}")
                print("-" * 30)

    # Search Contact
    elif choice == 3:
        search_name = input("Enter Name To Search: ")

        cursor.execute(
            "SELECT * FROM CONTACTS WHERE LOWER(name) = LOWER(?)",
            (search_name,)
        )

        result = cursor.fetchone()

        if result:
            print("\nContact Found")
            print(f"ID: {result[0]}")
            print(f"Name: {result[1]}")
            print(f"Phone: {result[2]}")
        else:
            print("Contact Not Found")

    # Exit
    elif choice == 4:
        print("Good Bye!")
        break

    else:
        print("Invalid Choice. Try Again.")

# Close connection
conn.close()

'''

Code	                     Meaning

sqlite3.connect()	      Open a database
CREATE TABLE	           Make a table
INSERT INTO	                Add data
SELECT	                    Read data
fetchone()	             Get one result
fetchall()	             Get all results
commit()	               Save changes

Many programmers learn this way:
'''