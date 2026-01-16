class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.bonus = 0.1

    def role(self):
        return "Manager"

    def get_salary(self):
        return self.salary + self.salary * self.bonus


employees = [
    Employee("Sasa", 100),
    Manager("Amina", 100000)
]

for e in employees:
    if e.role() == "Manager":
        print(f"Name: {e.name} | Role: {e.role()} | Salary: {e.get_salary()} $")
    else:
        print(f"Name: {e.name} | Role: {e.role()} | Salary: {e.salary} $")
