from abc import ABC, abstractmethod
import math
from typing import Type


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = self.validation(radius)

    @staticmethod
    def validation(radius):
        if isinstance(radius, (int, float)) and radius > 0:
            return radius
        else:
            raise TypeError("radius must be int or float and postive number ")

    def area(self):
        return round(math.pi*(self.radius**2), 2)

    def perimeter(self):
        return round(2*math.pi*self.radius, 2)


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = self.validation(length)
        self.width = self.validation(width)

    @staticmethod
    def validation(x):
        if isinstance((x), int) and x > 0:
            return x
        else:
            raise TypeError("must be postive integer")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.width + self.length)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = self.validation(a)
        self.b = self.validation(b)
        self.c = self.validation(c)

    @staticmethod
    def validation(x):
        if isinstance(x, int) and x > 0:
            return x
        else:
            raise TypeError("must be postive integer")

    def area(self):

        return self.a + self.b+self.c

    def perimeter(self):
        s = (self.a+self.b+self.c)/2
        Area = round(math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c)),2)
        return Area


try:
    circle1 = Circle(10)
    print(circle1.area())
    print(circle1.perimeter())

    rectangle = Rectangle(10, 14)
    print(rectangle.area())
    print(rectangle.perimeter())

    tri = Triangle(10, 12, 16)
    print(tri.area())
    print(tri.perimeter())

except TypeError as e:
    print(e)
except ValueError as e:
    print(e)


# can write validation as abstractmethod
