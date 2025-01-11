from __future__ import annotations
import datetime
import re
class Student:
    def __init__(self,student_id,name,dob):
        self.__student_id=student_id
        self.__name=name
        self.__dob=dob
        self.__gpa=0.0
    @property
    def student_id(self):
        return self.__student_id
    @property
    def name(self):
        return self.__name
    @property
    def dob(self):
        return self.__dob
    @property
    def gpa(self):
        return self.__gpa
    @gpa.setter
    def gpa(self,gpa):
        self.__gpa=gpa
    def list(self):
        print(f"SID: {self.__student_id} - Name: {self.__name} - DoB: {self.__dob} - GPA: {self.__gpa}")