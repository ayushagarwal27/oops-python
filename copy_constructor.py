class Student:
    def __init__(self, student=None):
        if student == None:
            self.__name = ""
            self.__age = 0
            
        else:
            self.__name = student.__name
            self.__age = student.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return f'{self.__name} : {self.__age}'


rahul = Student()
rahul.set_name('Rahul')
rahul.set_age(40)

rh = Student(rahul)
print(rahul)
print(rh)
