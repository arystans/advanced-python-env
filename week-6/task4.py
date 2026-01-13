class Employee:
    def __init__(self, salary):
        self._salary = salary  # private by convention

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus


def eeeinfo(employees):
    for emp in employees:
        print(f"Role: {emp.get_role()}, Salary: {emp.get_salary()}")


employees = [
    Employee(3000),
    Manager(5000, 1000)
]

eeeinfo(employees)
