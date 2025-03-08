from chap4.ex92.models.StudentManagementSystem import StudentManagementSystem

sms = StudentManagementSystem()

sms.add_class('C01', 'Python')
sms.add_student('S01', 'teo', 2000, 'C01')
sms.add_student('S02', 'ty', 2001, 'C01')
sms.add_subject('S01', 'Python Programming', 4)

loaded_data = StudentManagementSystem.load_data()
if loaded_data:
    sms = loaded_data
while True:
        print("\n===== Student Management System =====")
        print("1. View Course List")
        print("2. View Student List for a Course")
        print("3. View Subject List")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            sms.print_courses()
        elif choice == "2":
            course_id = input("Enter course ID: ")
            sms.print_students(course_id)
        elif choice == "3":
            for subject in sms.Subjects.values():
                print(subject)
        elif choice == "4":
            print("\nWhat do you want to add?")
            print("1. Add Course")
            print("2. Add Student")
            print("3. Add Subject")
            sub_choice = input("Enter choice: ")

            if sub_choice == "1":
                course_id = input("Enter course ID: ")
                course_name = input("Enter course name: ")
                sms.add_class(course_id, course_name)
            elif sub_choice == "2":
                student_id = input("Enter student ID: ")
                student_name = input("Enter student name: ")
                student_yob = int(input("Enter student year of birth: "))
                course_id = input("Enter course ID: ")
                sms.add_student(student_id, student_name, student_yob, course_id)
            elif sub_choice == "3":
                subject_id = input("Enter subject ID: ")
                subject_name = input("Enter subject name: ")
                num_credits = int(input("Enter number of credits: "))
                sms.add_subject(subject_id, subject_name, num_credits)
            sms.save_data()
        elif choice == "5":
            sms = StudentManagementSystem.load_data()
        elif choice == "6":
            print('Tks, bjtch~ Next!')
            break
        else:
            print("Invalid choice! Try again.")