from domains.management import Management
from input import *
from output import list_students, list_courses, list_marks 
import os
from compress import *
def main():
    menu=Management()
    load(menu)
    while(True):
        print("\n-----Student Management System-----")
        print("1.Input student info\n2.Input course info\n3.Input marks for a course\n4.List all courses\n5.List all students\n6.Show marks for a course")
        print("---------")
        print("7.Exit")
        try:
            choice=int(input("\n\nEnter your choice: "))
            match choice:
                case 1:
                    print("\nAdding students' info...")
                    student=student_input(existing_ids=menu.students.keys())
                    menu.add_stu(student)
                    save_data(menu)
                case 2:
                    print("\nAdding courses' info...")
                    course=course_input(existing_ids=menu.courses.keys())
                    menu.add_course(course)
                    save_data(menu)
                case 3:
                    print("\nAdding marks...")
                    course_id=input("Enter the course id: ")
                    if course_id not in menu.courses.keys():
                        print("Course ID's not found")
                        continue
                    if not menu.students.keys():
                        print("No students in the system")
                        continue
                    marks=mark_input(course_id,menu.students)
                    menu.add_mark(marks)
                    save_data(menu)
                case 4:
                    if not menu.courses.keys():
                        print("\nNo courses in the system yet")
                        continue
                    print("\nListing all courses...")                    
                    list_courses(menu.courses)
                case 5:
                    if not menu.students.keys():
                        print("\nNo students in the system yet")
                        continue
                    print("\nListing all students...")
                    menu.calculating_gpa()
                    sorted=menu.list_students()
                    list_students(sorted)
                case 6:
                    print("\nListing marks for a course...")
                    course_id=input("Enter the course id: ")
                    if course_id not in menu.courses.keys():
                        print("Course ID's not found")
                        continue
                    if course_id not in menu.marks.keys():
                        print("No marks for this course yet")
                        continue
                    list_marks(menu.marks[course_id],menu.students)
                case 7:
                    print("Exiting the program.")
                    os.system('cls' if os.name=='nt' else 'clear')
                    compress()
                    break
                case _:
                    print("Invalid choice. Pls try again")
        except ValueError:
            print("Enter an integer pls")
if __name__=="__main__":
    main()