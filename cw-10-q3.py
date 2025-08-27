from datetime import datetime
import json
from validator import (
    validate_email,
    validate_phone,
    validate_username,
)
import validate_exception


class IsNotInstance(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ReservetionSys:

    def __init__(self, admin):
        self.admin = admin

    @staticmethod
    def rent_car(customer, invoice, car):
        """
        args: customer instance customer invoice and a car instance
        output: check invoice time and allow user to rent based on time
        """

        try:
            if (
                isinstance(car, Car)
                and isinstance(customer, Customer)
                and isinstance(invoice, Invoice)
            ):
                time_duration = invoice.end - invoice.start
                time_duration = time_duration.days
                if time_duration > 0:

                    return customer.rent_car(car)

                return "rent by yourself or someone else"

            raise IsNotInstance("inputs are not instance of classes")
        except IsNotInstance as e:
            print(e)

    @staticmethod
    def cancel_car(customer, car):

        try:

            if isinstance(car, Car) and isinstance(customer, Customer):
                return customer.cancel_car(car)

            raise IsNotInstance("car or customer must be instance of car/customer")

        except IsNotInstance as e:
            print(e)

    @staticmethod
    def invoice_price(invoice):
        """
        arg:customer invoice

        function body: calculate invoice price and execute logging function

        return: invoice_price
        """
        try:

            if isinstance(invoice, Invoice) and invoice.customer.rented_car:
                invoice.clac_total_price()
                ReservetionSys.logging(invoice)
                print(invoice.total_rent_price)

            elif not isinstance(invoice, Invoice):
                raise IsNotInstance("invoice must be instance of invoice class")

            else:
                print("your contract time is over")
        except IsNotInstance as e:
            print(e)

    @staticmethod
    def logging(invoice):

        try:

            with open("car_reservetion_logs.json", "r", encoding="utf-8") and open(
                "car_reservetion_logs.json", "a", encoding="utf-8"
            ) as file:

                my_dict = {
                    invoice.id: {
                        invoice.customer.customer_id: list(
                            map(
                                lambda car: car.__dict__,
                                invoice.customer.rented_car,
                            )
                        )
                    },
                    "invoice_total_price": invoice.total_rent_price,
                    "time_duration": [
                        invoice.start.strftime("%Y,%m,%d"),
                        invoice.end.strftime("%Y,%m,%d"),
                    ],
                }

                json.dump(my_dict, file, indent=4)

        except TypeError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except KeyError as e:
            print(e)
        except IOError as e:
            print(f"Error opening or writing to file: {e}")

    @staticmethod
    def get_logs():
        """
        read logs from car reservation.json file
        """
        try:

            with open("car_reservetion_logs.json", "r", encoding="utf-8") as file:
                content = file.read()
                data = json.loads(content)
                print(data)

        except TypeError as e:
            print(e)
        except FileNotFoundError:
            print("Error: The file 'car_reservetion_logs.json' was not found.")
        except json.JSONDecodeError:
            print(
                "Error: Could not decode JSON from car_reservetion_logs.json. Check file content for valid JSON format."
            )


class Car:
    counter = 0
    car_list = []

    def __init__(self, brand, model, rent_prie, date):
        Car.counter += 1
        self.brand = brand
        self.modle = model
        self.rent_price = rent_prie
        self.date_of_manufactured = date
        self.id = f"{Car.counter}"
        self.status = False
        Car.car_list.append(self)

    @classmethod
    def show_car_li(cls):
        return cls.car_list

    def check_status(self, status):
        self.status = status


class Invoice:
    def __init__(self, start_date, end_date, user):
        self.id = self.__gen_id()
        self.start = start_date
        self.end = end_date
        self.customer = user
        self.total_rent_price = 0

    def clac_total_price(self):
        if len(self.customer.rented_car) < 0:
            return self.total_rent_price

        time_duration = self.end - self.start
        time_duration = time_duration.days
        total_price = 0

        for car in self.customer.rented_car:
            total_price += car.rent_price

        self.total_rent_price = total_price * time_duration

    @staticmethod
    def __gen_id():
        counter = 0
        counter += 1
        return f"{counter}"


class User:
    def __init__(self, email):

        self.email = self.__email_validate(email)

    def __email_validate(self, email):
        if validate_email(email):
            return email
        raise validate_exception.InvalidEmail("email format is not correct")


class Customer(User):
    def __init__(self, name, email, tel):
        super().__init__(email)
        self.customer_id = tel
        self.name = self.__name_validate(name)
        self.tel = self.__tel_validate(tel)
        self.rented_car = []

    def __name_validate(self, name):
        if validate_username(name):
            return name
        raise validate_exception.InvalidUsername(
            "username inclue upper case and lowercase char combine with number"
        )

    def __tel_validate(self, tel):
        if validate_phone(tel):
            return tel
        raise validate_exception.InvalidTelNumber("tel format is incorrect")

    def rent_car(self, car):
        if car.status is False and car not in self.rented_car:
            car.check_status(True)
            self.rented_car.append(car)
            return "car is rent successfuly"

    def show_cars(self):

        return self.rented_car

    def cancel_car(self, car):

        try:
            if car.status and car in self.rented_car:
                self.rented_car.remove(car)
                car.check_status(False)
                return "car is removed from your rented list"

            raise ValueError("this car is not in rent list")

        except ValueError as e:
            print(e)


class Admin(User):
    def __init__(self, email):
        super().__init__(email)
        self._admin_id = self.__gen_id()

    @staticmethod
    def __gen_id():
        today = datetime.now()
        today = str(today.timestamp())
        return today


admin1 = Admin("miladadmin@gmail.com")
admin2 = Admin("aliadmin@gmail.com")
customer1 = Customer("majidmk3", "majid@gmail.com", "09376330282")
customer2 = Customer("Aligoli01", "ali_goli@gmail.com", "09386542232")
customer3 = Customer("Rezadavoodi1", "reza@gmail.com", "09996542232")
car1 = Car("Ford", "Ford_2025", 6000, "2025, 2, 3")
car2 = Car("wolexwagn", "gul_3third_gen", 2000, "2022, 8, 3")
car3 = Car("BMW", "x7", 5000, "2025, 11, 3")
car4 = Car("BMW", "x5", 5000, "2025, 1 ,3")
car5 = Car("Benz", "c300_2023", 34000, "2023, 1, 3")


customer1_invoice = Invoice(datetime.now(), datetime(2025, 8, 25, 0, 0, 0), customer1)

customer2_invoice = Invoice(datetime.now(), datetime(2025, 8, 30, 0, 0, 0), customer2)
customer3_invoice = Invoice(datetime.now(), datetime(2025, 9, 1, 0, 0, 0), customer3)

rent_app = ReservetionSys(admin1)
print(rent_app.rent_car(customer1, customer1_invoice, car1))
print(rent_app.rent_car(customer1, customer1_invoice, car2))

print("customer1 ", customer1.show_cars())
print("customer1", rent_app.invoice_price(customer1_invoice))


rent_app.rent_car(customer2, customer2_invoice, car1)
rent_app.rent_car(customer2, customer2_invoice, car2)
print("customer2 ", customer2.show_cars())
print("customer2", rent_app.invoice_price(customer2_invoice))

rent_app.rent_car(customer3, customer3_invoice, car4)
rent_app.rent_car(customer3, customer3_invoice, car3)
print("customer3 ", customer3.show_cars())

print("customer3", rent_app.invoice_price(customer3_invoice))


print(rent_app.get_logs())
