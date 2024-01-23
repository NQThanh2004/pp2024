def input_number(prompt):
    return int(input(prompt))

def input_student_infor():
    student_id = input("Enter student ID:")
    student_name = input("Enter student name:")
    student_dob = input("Enter student date or birth:")
    return student_id, student_name, student_dob

def input_number_of_courses():
    return input_number("Enter the number of courses:")

def input_course_infor():
    course_id = input("Enter course ID:")
    course_name = input("Enter course name:")
    return course_id, course_name

def input_marks(courses):
    marks = {}
    for course_id, course_name in courses.items():
         mark = float(input(f"Enter mark for {course_name}:"))
         marks[course_id] = mark
    return marks

def list_courses(courses):
    print("courses:")
    for course_id, course_name in courses.items():
         print(f"{course_id}: {course_name}")

def list_students(students):
    print("Students:")
    for student_id, student_info in students.items():
        print(f"{student_id}: {student_info[0]} - {student_info[1]}")

def show_student_marks(students, courses, marks):
    student_id = input("Enter student ID: ")
    if student_id in students:
        student_info = students[student_id]
        print(f"Student ID: {student_id}")
        print(f"Student Name: {student_info[0]}")
        print("Marks:")
        for course_id, mark in marks.get(student_id, {}).items():
            print(f"{courses[course_id]}: {mark}")
    else:
        print("Student not found.")

def main():
    students = {}
    courses = {}
    student_marks = {}

    num_students = input_number("Enter the number of students in the class: ")

    for _ in range(num_students):
        student_id, student_name, student_dob = input_student_infor()
        students[student_id] = (student_name, student_dob)

    num_courses = input_number_of_courses()

    for _ in range(num_courses):
        course_id, course_name = input_course_infor()
        courses[course_id] = course_name

    while True:
        print("\n1. Input Marks\n2. List Courses\n3. List Students\n4. Show Student Marks\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            list_students(students)
            student_id = input("Select a student ID to input marks: ")
            if student_id in students:
                marks = input_marks(courses)
                student_marks[student_id] = marks
            else:
                print("Student not found.")
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            show_student_marks(students, courses, student_marks)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()