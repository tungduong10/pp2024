import os
from zipfile import ZipFile
from domains.student import Student
from domains.courses import Courses
from domains.marks import Marks
import datetime
import pickle
files = ["students.pkl", "courses.pkl", "marks.pkl"]

def file_path(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

def compress():
    try:
        if not any([os.path.exists(file_path(file)) for file in files]):
            print("\nNo files to compress!")
            return
        with ZipFile(file_path("students.zip"), "w") as zip:
            for file_name in files:
                full_path = file_path(file_name)
                if os.path.exists(full_path):
                    zip.write(full_path, file_name)
                    os.remove(full_path)
        print("\nFiles compressed successfully!")
    except Exception as e:
        print(f"\nAn error occurred during compression: {e}")

def decompress():
    try:
        zip_path = file_path("students.zip")
        if os.path.exists(zip_path):
            with ZipFile(zip_path, "r") as zip:
                zip.printdir()
                zip.extractall(os.path.dirname(zip_path))
            os.remove(zip_path)
            print("\nFiles decompressed successfully!")
        else:
            print("\nNo files to decompress!")
    except Exception as e:
        print(f"\nAn error occurred during decompression: {e}")

def load(menu):
    try:
        if os.path.exists(file_path(files[0])):
            with open(file_path(files[0]),"rb") as f:
                students=pickle.load(f)
                for student_id in students.keys():
                    menu.add_stu(students[student_id])
        if os.path.exists(file_path(files[1])):
            with open(file_path(files[1]),"rb") as f:
                courses=pickle.load(f)
                for course_id in courses.keys():
                    menu.add_course(courses[course_id])
        if os.path.exists(file_path(files[2])):
            with open(file_path(files[2]),"rb") as f:
                marks=pickle.load(f)
                for course_id in marks.keys():
                    menu.add_mark(marks[course_id])  
    except Exception as e:
        print(f"\nAn error occurred during loading: {e}")