from typing import Any, Optional, Union, Tuple

name: Any = 'Ayush'
print(name)

age: Optional[int] = None
age = 10
print(age)

email_or_phone: Union[str, int] = 'aysuh@email.com'
email_or_phone = 984984948
print(email_or_phone)

car_and_model: Tuple[str, str] = ('BME', 'X947U')


def greet(name: str) -> None:
    print('Hello!', name)


greet('Ayush')


class Student:
    def __init__(self, name):
        self.__name: str = name

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name


raj = Student('Ayush')
raj.set_name('Raju')
print(raj.get_name())
