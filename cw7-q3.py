from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_vehicle(self):
        pass


class Car_Factory(Factory):
    def create_vehicle(self):
        return "car is created"


class Bike_Factory(Factory):
    def create_vehicle(self):
        return "bike is created"


def get_type(param):
    if param.lower() == "car":
        return Car_Factory()
    else:
        return Bike_Factory()


car = get_type("Car")
bike = get_type("bike")
print(car.create_vehicle())
print(bike.create_vehicle())
