import math
class Marks:
    def __init__(self,course_id):
        self.__course_id=course_id
        self.__student_marks={}
    @property
    def course_id(self):
        return self.__course_id
    def get_student_marks(self):
        return self.__student_marks
    def add_mark(self,student_id,mark):
        self.__student_marks[student_id]=mark
    def list(self,students):
        print(f"Marks for course {self.__course_id}")
        for student_id,mark in self.__student_marks.items():
            print(f"ID: {student_id} ({students[student_id].name}): {mark}")