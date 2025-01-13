class Courses:
    def __init__(self,course_id,name,credits):
        self.__course_id=course_id
        self.__name=name
        self.__credits=credits
    @property
    def course_id(self):
        return self.__course_id
    @property
    def name(self):
        return self.__name
    @property
    def credits(self):
        return self.__credits
    def list(self):
        print(f"CID: {self.__course_id} - Name: {self.__name} - Credits: {self.__credits}")