from validator import (
    validate_email,
    validate_password,
    validate_phone,
    validate_username,
)
import validate_exception
from datetime import datetime


class User:
    def __init__(self, username, password, email, tel):
        self.username = self.check_username(username)
        self.__password = self.password = password
        self.__email = self.email = email
        self.__tel = self.tel = tel

    def check_username(self, username):

        try:

            if validate_username(username):
                return username

            raise validate_exception.InvalidUsername("username format is not accepted")

        except validate_exception.InvalidUsername as e:
            print(e)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):

        try:

            if validate_password(password):
                self.__password = password

            else:
                raise validate_exception.InvalidPassword(
                    "password must have 8char and include upper and lowercase"
                )
        except validate_exception.InvalidPassword as e:
            print(e)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):

        try:
            if validate_email(email):
                self.__email = email
                print("email is correct")

            raise validate_exception.InvalidEmail(
                "email include symbole @.+_ and number and upper and lower char and org|com suffix"
            )
        except validate_exception.InvalidEmail as e:
            print(e)

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, tel):
        if validate_phone(tel):
            self.__tel = tel
        else:
            raise validate_exception.InvalidTelNumber(
                "must be 14 char inclues number 1-9"
            )


class Task:

    def __init__(self, title, desc, start_time, end_time):
        self.title = title
        self.desc = desc
        self.start = start_time
        self.end = end_time
        self.status = "todo"
        self.change = []

    def __str__(self):
        return f"task_title:{self.title} task_desc:{self.desc} task_start:{self.start} task_end:{self.end}"

    def change_status(self, status):
        self.status = status

    def check_end_time(self):
        pass


class Taskmanager:
    def __init__(
        self,
    ):
        self.tasks = []
        self.user = ""

    def add_task(self, user, task):
        pass

    def __repr__(self):
        pass

    def search_tasks(slef):
        pass

    def filter_task(slef):
        pass

    def sign_up(self, username, email, tel, password):
        try:

            new_user = User(username, password, email, tel)
            if isinstance(new_user, User):
                self.user = new_user
            raise IsNotInstance("user")
        except Exception as e:
            print(e)

    def sign_in(self, username, password):
        pass

    def edit_task(self):
        pass

    def delete_taks(self):
        pass


class IsNotInstance(Exception):
    def __init__(self, msg):
        super().__init__(msg)


user1 = User("MAjidmk9", "123M@j!d1215", "majid@gmail.com", "9376133028")
print(user1.tel)
