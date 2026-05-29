                                                                # STUDENT MANAGEMENT SYSTEM

students = []

print("===== WELCOME TO STUDENT MANAGEMENT SYSTEM =====")

while True:

    print("\n======= MENU =======")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    # ADD STUDENT
    if choice == 1:

        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        # STUDENT DICTIONARY
        student = {
            'name': name,
            'age': age,
            'course': course,
            'marks': marks
        }

        # ADD STUDENT TO LIST
        students.append(student)

        print("Student Added Successfully!")

    # VIEW ALL STUDENTS
    elif choice == 2:

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\n===== ALL STUDENTS =====")

            for i in students:

                print(f"{i['name']} | {i['age']} | {i['course']} | {i['marks']}")

    # SEARCH STUDENT
    elif choice == 3:

        search = input("Enter Student Name: ")

        found = False #IT'S A BOOLEAN VARIABLE MEANS IF STUDENT IS NOT FOUND

        for i in students:

            if i["name"] == search:

                print("\nStudent Found:")
                print(i)

                found = True

            if found == False:
                print("Student Not Found")

    # EXIT
    elif choice == 4:

        print("Thanks For Using Student Management System")
        break

    # INVALID CHOICE
    else:
        print("Invalid Choice")