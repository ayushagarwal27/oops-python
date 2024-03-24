class Student:
    def __init__(self, name, age, subject):
        self.__name = name  # Private(__var)
        self.age = age  # Public
        self._subject = subject  # Protected (_var)

    def getName(self):
        return self.__name

    # Private method
    def __change_age(self, age):
        self.age = age


raj = Student('Raj', 32, 'Maths')
print(raj._subject)
