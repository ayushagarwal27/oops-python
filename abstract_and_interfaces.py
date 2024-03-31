from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_email(self):
        pass


class User(Person):

    def get_email(self):
        return 'as@email.com'

    def get_name(self):
        return 'No Name'


rahul = User()
