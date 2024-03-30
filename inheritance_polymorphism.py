class User:

    def __init__(self, username):
        self._username = username

    def login(self):
        print('Logging in as', self._username)


class Instructor(User):
    def __init__(self, username, subject):
        super().__init__(username)
        self.subject = subject

    def login(self):
        print(f'Logging in as instructor: {self._username} who teaches {self.subject}', )


mohit = Instructor('Mohit', 'Maths')
mohit.login()
