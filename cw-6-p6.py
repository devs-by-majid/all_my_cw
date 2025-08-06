
def role_checker(func):
    def wrapper(self, *args, **kwargs):
        if self.user.role == "developer":
            print("you don't have permission")
            return
        if self.user.role == "manager":
            result = func(self, *args, **kwargs)
            return result
    return wrapper


class ProjectSystem:

    def __init__(self, projectname, user):
        self.user = user
        self.__project = projectname

    @role_checker
    def delete_project(self):
        del self.__project

    @role_checker
    def view_project(self):
        return f"{self.__project}"


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class Developer(User):
    pass


class Manager(User):
    pass


try:
    devloper1 = Developer("majid", "developer")
    manager1 = Manager("mohsen", "manager")
    project1 = ProjectSystem("onlineshop_landingpage", devloper1)

    print(project1.delete_project())
    print(project1.view_project())

except AttributeError as e:
    print(e)
except Exception as e:
    print(e)
