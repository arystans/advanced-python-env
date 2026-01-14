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


def winfo(employees):
    for emp in employees:
        print("Role: " + emp.get_role() + " Salary: " + str(emp.get_salary()))


employees = []

n = int(input("How many employees? "))

for i in range(n):
    role = input("Enter role (employee/manager): ").lower()
    salary = int(input("Enter salary: \n"))

    if role == "manager":
        bonus = int(input("Enter bonus: "))
        employees.append(Manager(salary, bonus))
    else:
        employees.append(Employee(salary))

winfo(employees)
print(Manager.get_bonus(self=employees[0]))
