class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce_person(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}")


class Employee(Person):


    def __init__(self, first_name, last_name, job_type):
        super().__init__(first_name, last_name)
        self.job_type = job_type

    def introduce_person(self):
        print(f"Hello, my name is {self.first_name} {self.last_name}, working as a {self.job_type}")

    def work(self):
        print(f"{self.first_name} working as a {self.job_type}")

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    def __eq__(self, other_object):
        if isinstance(other_object, Employee):
            return self.last_name == other_object.last_name and self.first_name == other_object.first_name
        return False

person_1 = Person(first_name = "John", last_name="Smith")
print(person_1)
person_1.introduce_person()
#person_1.work()

employee_1 = Employee(first_name="Jack", last_name="Lumber", job_type="developer")
employee_2 = Employee(first_name="Jack", last_name="Lumber", job_type="developer")
print(employee_1)
employee_1.introduce_person()
employee_1.work()
print("---------------------")
print(employee_1 == employee_2)
