class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # private attribute

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self._bonus = 0.1

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self._salary * self._bonus

    def get_salary(self):
        return self._salary + self.get_bonus()


def print_employees(employees):
    for e in employees:
        print(f"Name: {e.name} | Role: {e.get_role()} | Salary: {e.get_salary()} $")


employees = [
    Employee("Sasa", 100),
    Manager("Amina", 100000)
]

print_employees(employees)

