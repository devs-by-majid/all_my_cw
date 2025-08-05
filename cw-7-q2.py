
class ReperMixin:

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ', '.join(
            f'{key}={value!r}' for key, value in self.__dict__.items())
        return f'{class_name}({attributes})'


class Book(ReperMixin):
    def __init__(self, book_name, title):
        self.name = book_name
        self.title = title


class Car(ReperMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price


car1 = Car("Toyota", 1200000)
book1 = Book("everything is fucked", "self_help")

print(car1)
print(book1)
