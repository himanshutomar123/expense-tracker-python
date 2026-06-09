contacts = []

def add_contact():
    name = input("ENTER YOUR NAME: ")
    mob = input("ENTER YOUR NUMBER: ")

    contact = {
        'name': name,
        'mob': mob
    }

    contacts.append(contact)
    print("CONTACT ADDED SUCCESSFULLY")


def view_contact():
    if not contacts:
        print("NO CONTACT FOUND")
    else:
        print("\n=========== CONTACT LIST ===========")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. NAME: {contact['name']} | MOBILE NUMBER: {contact['mob']}")


def search_contact():
    search_name = input("ENTER NAME TO SEARCH: ")

    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            print("\nCONTACT FOUND")
            print(f"NAME: {contact['name']}")
            print(f"MOBILE NUMBER: {contact['mob']}")
            return

    print("CONTACT NOT FOUND")


def edit_contact():
    edit_name = input("ENTER NAME TO EDIT: ")

    for contact in contacts:
        if contact['name'].lower() == edit_name.lower():
            print("CONTACT FOUND")

            new_name = input("ENTER NEW NAME: ")
            new_mob = input("ENTER NEW MOBILE NUMBER: ")

            contact['name'] = new_name
            contact['mob'] = new_mob

            print("CONTACT EDITED SUCCESSFULLY")
            return

    print("CONTACT NOT FOUND")


def delete_contact():
    delete_name = input("ENTER NAME TO DELETE: ")

    for contact in contacts:
        if contact['name'].lower() == delete_name.lower():
            contacts.remove(contact)
            print("CONTACT DELETED SUCCESSFULLY")
            return

    print("CONTACT NOT FOUND")


while True:

    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice = int(input("ENTER YOUR CHOICE: "))
    except ValueError:
        print("PLEASE ENTER A VALID NUMBER")
        continue

    if choice == 1:
        print("DEBUG: ADD CONTACT CALLED")  # optional check
        add_contact()

    elif choice == 2:
        view_contact()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        edit_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        print("THANK YOU FOR USING CONTACT BOOK")
        break

    else:
        print("INVALID CHOICE")
