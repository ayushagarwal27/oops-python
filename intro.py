class Student:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def change_subject(self, new_subject):
        self.subject = new_subject

    def walk(self):
        print(f'{self.name} is walking...')


abhinav = Student('Abhinav', 90, 'Maths')
ravi = Student('Ravi', 26, 'Computer Science')

print(abhinav.subject)
print(ravi.subject)

Student.change_subject(abhinav, 'Politics')
ravi.change_subject('English')

print(abhinav.subject)
print(ravi.subject)
