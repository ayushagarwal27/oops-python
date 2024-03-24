class Student:
    def __init__(self, name, age):
        self.__enrolled = True
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name


ravi = Student('Ravi', 20)
