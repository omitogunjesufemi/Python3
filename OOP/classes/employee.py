class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

Employee.set_raise_amount(1.06)

employee_1 = Employee("Corey", "Schafer", 50000)
employee_2 = Employee("Test", "Employee", 60000)

print(Employee.raise_amount)
print(Employee.num_of_employees)
print(employee_1.raise_amount)
print(employee_2.raise_amount)
