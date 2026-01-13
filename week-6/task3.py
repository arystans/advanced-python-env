#OOP
class Person:
    def __init__(self, name):
        self._name = name  # encapsulation

    def get_info(self):
        return f"Person name: {self._name}"


class Student(Person):
    def __init__(self, name, s_id):
        super().__init__(name)
        self.s_id = s_id

    def get_info(self):  # polymorphism
        return f"Student name: {self._name}, ID: {self.s_id}"


person = Person("John")
student = Student("Alice", "S123")

print(person.get_info())
print(student.get_info())
