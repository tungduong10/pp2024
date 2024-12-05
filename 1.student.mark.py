import datetime
import re
import os
students={}
courses={}
marks={}

def add_student():
    print("\nAdding students' info...")
    no_student=int(input("Enter the number of student you want to add: "))
    for i in range(no_student):
        name=input(f"Enter the {i+1}th student's name: ")
        student_id=input(f"Enter the student id for student {i+1}: ")
        while(True):
            if not re.match(r"\d{2}BI\d{2}-\d{3}", student_id):
                student_id=input("Invalid ID! Pls enter valid ID: ")
                continue
            if student_id in students:
                student_id=input("Student ID alr exists! Pls enter unique ID: ")
                continue
            break
        while(True):
            h=input("Enter the date of birth (following yyyy-mm-dd format ): ")
            try:
                if not re.match(r"\d{4}-\d{2}-\d{2}",h):
                    h=input("Invalid format! Pls re-enter: ")
                y,M,d=map(int,h.split("-"))
                dob=datetime.date(y,M,d)
                break
            except ValueError:
                print("Invalid date! Pls enter a valid one: ")
        students[student_id]=(name,dob)

def add_course():
    print("\nAdding courses' info...")
    no_course=int(input("Enter the number of courses you want to add: "))
    for i in range(no_course):
        course_id=input(f"Enter course ID for the {i+1}th course: ")
        while(True):
            if course_id in courses:
                course_id=input("Course ID alr exists! Pls enter unique course ID: ")
                continue
            break
        course_name=input(f"Enter course name for the {i+1}th course: ")
        while(True):
            if any(x==course_name for x in courses.values()):
                course_name=input("Course alr exists! Pls enter unique course: ")
                continue
            break
        courses[course_id]=(course_name)
                
def add_mark():
    print("\nAdding marks...")
    while(True):
        course_id=input("Enter course ID to access: ")
        if course_id not in courses:
            while(True):
                print("Course ID not found")
                print("1.Retry\n2.Exit")
                try:
                    choice=int(input("Enter your choice: "))
                    if choice==1:
                        course_id=input("Enter course ID: ")
                    elif choice==2:
                        print("Exiting...")
                        return
                    else:
                        print("Invalid choice! Pls enter 1 or 2")
                except ValueError:
                    print("Pls enter an integer")
        else:
            break
            
    if course_id not in marks:
        marks[course_id]={}
    for student_id in students:
        while(True):
            try:
                mark=float(input(f"Enter the mark for student {student_id} ({students[student_id][0]}): "))
                marks[course_id][student_id]=(mark)
                break
            except ValueError:
                print("Pls enter the right datatype")
    print("Marks successfully added")

def show_courses():
    print("\nCourses:")
    for course_id,course_name in courses.items():
        print(f"CID: {course_id}: {course_name}")

def show_students():
    print("\nStudents:")
    for student_id,(name,dob) in students.items():
        print(f"SID: {student_id} - Name: {name} - DOB: {dob}")
        
def show_student_marks():
    print("\nShow students' marks...")
    while(True):
        course_id=input("Enter course ID to access: ")
        if course_id not in courses:
            while(True):
                print("Course ID not found")
                print("1.Retry\n2.Exit")
                try:
                    choice=int(input("Enter your choice: "))
                    if choice==1:
                        course_id=input("Enter course ID: ")
                    elif choice==2:
                        print("Exiting...")
                        return
                    else:
                        print("Invalid choice! Pls enter 1 or 2")
                except ValueError:
                    print("Pls enter an integer")
        else:
            break
    for student_id,mark in marks[course_id].items():
        print(f"ID: {student_id} ({students[student_id][0]}): {mark}")

def menu():
    while(True):
        print("\n-----Student Management System-----")
        print("1.Input student info\n2.Input course info\n3.Input marks for a course\n4.List all courses\n5.List all students\n6.Show marks for a course")
        print("---------")
        print("7.Exit")
        try:
            choice=int(input("\n\nEnter your choice: "))
            match choice:
                case 1:
                    add_student()
                case 2:
                    add_course()
                case 3:
                    add_mark()
                case 4:
                    show_courses()
                case 5:
                    show_students()
                case 6:
                    show_student_marks()
                case 7:
                    print("Exiting the program.")
                    os.system('cls' if os.name=='nt' else 'clear')
                    break
                case _:
                    print("Invalid choice. Pls try again")
        except ValueError:
            print("Enter an integer pls")

menu()