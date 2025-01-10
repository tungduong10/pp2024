import datetime
import re
import os
class Student:
    def __init__(self,student_id,name,dob):
        self.__student_id=student_id
        self.__name=name
        self.__dob=dob
    @property
    def student_id(self):
        return self.__student_id
    @property
    def name(self):
        return self.__name
    @property
    def dob(self):
        return self.__dob
    @staticmethod
    def input(existing_ids):
        name=input("Enter the student's name: ")
        while(True):
            student_id=input("Enter the student id: ")
            if not re.match(r"\d{2}BI\d{2}-\d{3}", student_id):
                student_id=input("Invalid ID! Pls enter valid ID: ")
                continue
            if student_id in existing_ids:
                print("Student ID alr exists! Pls enter unique ID: ")
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
    def list(self):
        print(f"SID: {self.__student_id} - Name: {self.__name} - DoB: {self.__dob}")

class Courses:
    def __init__(self,course_id,name):
        self.__course_id=course_id
        self.__name=name
    @property
    def course_id(self):
        return self.__course_id
    @property
    def name(self):
        return self.__name
    @staticmethod
    def input(existing_ids):
        while(True):
            course_id=input("Enter course ID for the course: ")
            if course_id in existing_ids:
                print("Course ID alr exists! Pls enter unique course ID!")
                continue
            break
        name=input(f"Enter course name for the course: ")
        return Courses(course_id,name)
    def list(self):
        print(f"CID: {self.__course_id} - Name: {self.__name}")

class Marks:
    def __init__(self,course_id):
        self.__course_id=course_id
        self.__student_marks={}
    @property
    def course_id(self):
        return self.__course_id
    
    def add_mark(self,student_id,mark):
        self.__student_marks[student_id]=mark
    @staticmethod
    def input(course_id,students):
        mark_obj=Marks(course_id)
        for student_id, student in students.items():
            while(True):
                try:
                    mark=float(input(f"Enter the mark for {student_id}/{student.name}: "))
                    mark_obj.add_mark(student_id,mark)
                    break
                except ValueError:
                    print("invalid! Pls enter a number")
        return mark_obj
    def list(self,students):
        print(f"Marks for course {self.__course_id}")
        for student_id,mark in self.__student_marks.items():
            print(f"ID: {student_id} ({students[student_id].name}): {mark}")

class Management:
    def __init__(self):
        self.students={}
        self.courses={}
        self.marks={}
    def add_stu(self):
        print("\nAdding students' info...")
        student=Student.input(existing_ids=self.students.keys())
        self.students[student.student_id]=student
    def add_course(self):
        print("\nAdding courses' info...")
        course=Courses.input(existing_ids=self.courses.keys())
        self.courses[course.course_id]=course
    def add_mark(self):
        print("\nAdding marks...")
        course_id=input("Enter the course id: ")
        if course_id not in self.courses.keys():
            print("Course ID's not found")
            return
        mark_obj=Marks.input(course_id,self.students)
        self.marks[course_id]=mark_obj
    def list_students(self):
        print("\nShowing all students...")
        for student in self.students.values():
            student.list()
    def list_courses(self):
        print("\nShowing all courses...")
        for course in self.courses.values():
            course.list()
    def list_marks(self):
        print("\nShowing marks for course?")
        course_id=input("Enter the course id: ")
        if course_id not in self.courses.keys():
            print("Course ID's not found")
            return
        self.marks[course_id].list(self.students)
    def menu(self):
        while(True):
            print("\n-----Student Management System-----")
            print("1.Input student info\n2.Input course info\n3.Input marks for a course\n4.List all courses\n5.List all students\n6.Show marks for a course")
            print("---------")
            print("7.Exit")
            try:
                choice=int(input("\n\nEnter your choice: "))
                match choice:
                    case 1:
                        self.add_stu()
                    case 2:
                        self.add_course()
                    case 3:
                        self.add_mark()
                    case 4:
                        self.list_courses()
                    case 5:
                        self.list_students()
                    case 6:
                        self.list_marks()
                    case 7:
                        print("Exiting the program.")
                        os.system('cls' if os.name=='nt' else 'clear')
                        break
                    case _:
                        print("Invalid choice. Pls try again")
            except ValueError:
                print("Enter an integer pls")  
                
if __name__=="__main__":
    system=Management()
    system.menu()