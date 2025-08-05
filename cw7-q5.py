from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def salary(self, h_payment):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, work_time):
        self.name = name
        self.work_time = work_time

    def salary(self, h_payment=10000):
        return self.work_time * h_payment


class SalariedEmployee(Employee):
    def __init__(self, name, wk):
        self.name = name
        self.work_time = wk

    def salary(self, h_payment=20000):
        return self.work_time * h_payment


class Manager(Employee):
    def __init__(self, name, wk, benefit):
        self.name = name
        self.work_time = wk
        self.benefit = benefit

    def salary(self, h_payment=50000):
        return self.work_time * h_payment + self.benefit


class Excutive(Employee):
    def __init__(self, name, wk, benefit):
        self.name = name
        self.work_time = wk
        self.benefit = benefit

    def salary(self, h_payment=40000):
        return self.work_time * h_payment + self.benefit


class Company:
    def __init__(self):
        self.employees = []

    def fire_employee(self, name=None):
        employee_names = filter(lambda emp: emp.name, self.employees)
        if name and name in employee_names:
            fired = filter(lambda employee: employee.name !=
                           name, self.employees)
            self.employees = fired
            return self.employees

    def hire_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        return "employee is already work here"

    def raise_employee(self, employee=None, value=None):
        if employee and value:
            for emp in self.employees:
                if employee.name == emp.name:
                    return emp.salary(value)

# setter Getter


he1 = HourlyEmployee("Ali", 10)
he2 = HourlyEmployee("morteza", 5)
se1 = SalariedEmployee("mehdi", 8)
se2 = SalariedEmployee("karim", 8)
m1 = Manager("majid", 18, 40000)
e1 = Excutive("milad", 17, 3000)


company1 = Company()
# print(company1.fire_employee())
print(company1.hire_employee(se2))
print(company1.hire_employee(he1))
print(company1.hire_employee(he2))
# print(company1.empolyees)
# print(he2.salary())
# print(company1.raise_employee(he2, 50000))

# print(se1.salary())
# print(company1.raise_employee(se1, 25000))

print(company1.employees)
# company1.fire_employee("Ali")
# company1.fire_employee("changiz")
# print(company1.hire_employee(se1))
