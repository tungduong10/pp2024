import math
import datetime
import re
from domains.student import Student
from domains.courses import Courses
from domains.marks import Marks
import pickle
from compress import *
def student_input(existing_ids):
    name=input("Enter the student's name: ")
    while(True):
        student_id=input("Enter the student id: ")
        if not re.match(r"\d{2}BI\d{2}-\d{3}", student_id):
            print("Invalid ID! Pls enter valid ID!")
            continue
        if student_id in existing_ids:
            print("Student ID alr exists! Pls enter unique ID! ")
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
            print("Invalid date! Pls enter a valid one!")
    return Student(student_id,name,dob)
def course_input(existing_ids):
    while(True):
            course_id=input("Enter course ID for the course: ")
            if course_id in existing_ids:
                print("Course ID alr exists! Pls enter unique course ID!")
                continue
            break
    name=input(f"Enter course name for the course: ")
    while(True):
        try:
            credits=int(input("Enter the number of credits for the course: "))
            break
        except ValueError:
            print("Invalid! Pls enter a integer")
    return Courses(course_id,name,credits)
def mark_input(course_id,students):
    mark_obj=Marks(course_id)
    for student_id, student in students.items():
        while(True):
            try:
                mark=float(input(f"Enter the mark for {student_id}/{student.name}: "))
                mark=math.floor(mark*10)/10
                mark_obj.add_mark(student_id,mark)
                break
            except ValueError:
                print("invalid! Pls enter a number")
    return mark_obj
def pickle_students(students):
    with open(file_path("students.pkl"),"wb") as f:
        pickle.dump(students,f)
def pickle_courses(courses):
    with open(file_path("courses.pkl"),"wb") as f:
        pickle.dump(courses,f)
def pickle_marks(marks):
    with open(file_path("marks.pkl"),"wb") as f:
        pickle.dump(marks,f)