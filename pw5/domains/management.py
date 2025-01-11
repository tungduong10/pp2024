import numpy as np
from domains.student import Student
from domains.courses import Courses
from domains.marks import Marks

class Management:
    def __init__(self):
        self.students={}
        self.courses={}
        self.marks={}
    def add_stu(self,student):
        self.students[student.student_id]=student
    def add_course(self,course):
        self.courses[course.course_id]=course
    def add_mark(self,mark):
        self.marks[mark.course_id]=mark
    def calculating_gpa(self):
        for student_id in self.students.keys():
            marks = []
            credits = []
            for course_id, course in self.courses.items():
                if course_id in self.marks and student_id in self.marks[course_id].get_student_marks():
                    marks.append(self.marks[course_id].get_student_marks()[student_id])
                    credits.append(course.credits)
            if credits:  
                self.students[student_id].gpa = round(np.average(marks, weights=credits),2)
            else:
                self.students[student_id].gpa=0.0
    def list_students(self):
        self.calculating_gpa()
        return sorted(self.students.values(),key=lambda x:x.gpa,reverse=True)