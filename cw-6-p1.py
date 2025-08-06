class User:
    def __init__(self, name):
        self.name = name
        self.__password = None

    @property
    def password(self):
        return f'{self.__password[5:]}{5*"*"}'

    @password.setter
    def password(self, value):
        if isinstance(value, str) and len(value) >= 8:
            self.__password = value
        else:
            raise TypeError("password must be string and at least 8 character")


try:
    user1 = User("majid")
    user1.password = "Majid_12345"
    print(user1.password)


except AttributeError as e:
    print(e)
except TypeError as e:
    print(e)
