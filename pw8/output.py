def list_students(students):
    print("\nStudents List:")
    for student in students:
        student.list()
def list_courses(courses):
    print("\nCourses List:")
    for course in courses.values():
        course.list()
def list_marks(marks, students):
    print("\nMarks List:")
    return marks.list(students)
