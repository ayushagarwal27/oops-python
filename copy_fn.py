class Student:
    def __init__(self, name):
        self.__name = name

    def copy(self):
        return Student(self.__name)


kesha = Student('Kesha')
ks = kesha.copy()

print(id(kesha) == id(ks))
