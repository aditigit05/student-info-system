from tabulate import tabulate

students = []
courses = ['Mathematics', 'Physics', 'Computer Science', 'Economics', 'Business Studies']

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. View Student by ID")
    print("6. Assign Courses")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':  # Add Student
        student = {}
        student['id'] = len(students) + 1
        student['enrollment_number'] = f"ENR{1000 + len(students)}"

        name = input("Enter Name: ").strip()
        if not name:
            print("Name is required.")
            continue
        student['name'] = name

        email = input("Enter Email: ").strip()
        if not email:
            print("Email is required.")
            continue
        if any(s['email'] == email for s in students):
            print("Email must be unique.")
            continue
        student['email'] = email

        phone = input("Enter Phone: ").strip()
        if not phone:
            print("Phone is required.")
            continue
        student['phone'] = phone

        address = input("Enter Address: ").strip()
        if not address:
            print("Address is required.")
            continue
        student['address'] = address

        print("\nSelect a Program:")
        programs = ['B.Tech', 'BBA', 'MCA']
        for i, program in enumerate(programs, 1):
            print(f"{i}. {program}")
        program_choice = input("Enter program choice number: ").strip()
        if program_choice not in ['1', '2', '3']:
            print("Invalid program choice.")
            continue
        student['program'] = programs[int(program_choice) - 1]

        print("\nSelect a Stream:")
        streams = ['Computer Science', 'Mechanical', 'Electronics', 'Management']
        for i, stream in enumerate(streams, 1):
            print(f"{i}. {stream}")
        stream_choice = input("Enter stream choice number: ").strip()
        if stream_choice not in ['1', '2', '3', '4']:
            print("Invalid stream choice.")
            continue
        student['stream'] = streams[int(stream_choice) - 1]

        student['courses'] = []
        students.append(student)
        print("Student added successfully.")

    elif choice == '2':  # Update Student
        student_id = input("Enter student ID to update: ").strip()
        student = next((s for s in students if str(s['id']) == student_id), None)

        if not student:
            print("Invalid ID. No student found.")
            continue

        new_name = input("Enter new Name (leave blank to keep unchanged): ").strip()
        if new_name:
            student['name'] = new_name

        new_email = input("Enter new Email (leave blank to keep unchanged): ").strip()
        if new_email and all(s['email'] != new_email for s in students):
            student['email'] = new_email
        elif new_email:
            print("Email must be unique.")
            continue

        new_phone = input("Enter new Phone (leave blank to keep unchanged): ").strip()
        if new_phone:
            student['phone'] = new_phone

        print("Student updated successfully.")

    elif choice == '3':  # Delete Student
        student_id = input("Enter student ID to delete: ").strip()
        student = next((s for s in students if str(s['id']) == student_id), None)

        if not student:
            print("Invalid ID. No student found.")
            continue

        students.remove(student)
        print("Student deleted successfully.")

    elif choice == '4':  # View All Students
        if not students:
            print("No student data available.")
        else:
            headers = ['ID', 'Enrollment Number', 'Name', 'Email', 'Phone', 'Address', 'Program', 'Stream', 'Courses']
            table = [[s['id'], s['enrollment_number'], s['name'], s['email'], s['phone'], s['address'], s['program'], s['stream'], ', '.join(s['courses'])] for s in students]
            print(tabulate(table, headers=headers, tablefmt="grid"))

    elif choice == '5':  # View Student by ID
        student_id = input("Enter student ID to view: ").strip()
        student = next((s for s in students if str(s['id']) == student_id), None)

        if not student:
            print("Invalid ID. No student found.")
        else:
            print("\nStudent Details:")
            for key, value in student.items():
                if key == 'courses':
                    print(f"{key.capitalize()}: {', '.join(value)}")
                else:
                    print(f"{key.capitalize()}: {value}")

    elif choice == '6':  # Assign Courses
        student_id = input("Enter student ID to assign courses: ").strip()
        student = next((s for s in students if str(s['id']) == student_id), None)

        if not student:
            print("Invalid ID. No student found.")
            continue

        print("Available courses:")
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course}")

        selected_courses = input("Enter course numbers separated by commas: ").strip().split(',')
        for num in selected_courses:
            if num.strip().isdigit() and 1 <= int(num.strip()) <= len(courses):
                course = courses[int(num.strip()) - 1]
                if course not in student['courses']:
                    student['courses'].append(course)

        print("Courses assigned successfully.")

    elif choice == '7':  # Exit
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")