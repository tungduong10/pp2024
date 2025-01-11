import os
from zipfile import ZipFile
from domains.student import Student
from domains.courses import Courses
from domains.marks import Marks
import datetime
files = ["students.txt", "courses.txt", "marks.txt"]

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
            with open(file_path(files[0]),"r") as f:
                for line in f:
                    parts=line.strip().split(" - ")
                    student_id=parts[0].split(": ")[1]
                    name=parts[1].split(": ")[1]
                    raw_dob=parts[2].split(": ")[1]
                    y,M,d=map(int,raw_dob.split("-"))
                    dob=datetime.date(y,M,d)
                    menu.add_stu(Student(student_id,name,dob))
        if os.path.exists(file_path(files[1])):
            with open(file_path(files[1]),"r") as f:
                for line in f:
                    parts=line.strip().split(" - ")
                    course_id=parts[0].split(": ")[1]
                    name=parts[1].split(": ")[1]
                    credits=int(parts[2].split(": ")[1])
                    menu.add_course(Courses(course_id,name,credits))
        if os.path.exists(file_path(files[2])):
            with open(file_path(files[2]),"r") as f:
                current_course_id=None
                for line in f:
                    if line.startswith("Marks for course"):
                        current_course_id=line.split(" ")[-1].strip().split(":")[0]
                        menu.marks[current_course_id]=Marks(current_course_id)
                    elif current_course_id and line.startswith("ID:"):
                        parts=line.strip().split(": ")
                        student_id=parts[1].split(" ")[0]
                        mark=float(parts[2])
                        menu.marks[current_course_id].add_mark(student_id,mark)          
    except Exception as e:
        print(f"\nAn error occurred during loading: {e}")