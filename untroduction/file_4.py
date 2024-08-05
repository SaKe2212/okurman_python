class Person:
    def __init__(self, name):
        self.__name = name


    @property
    def name(self):
        return self.name


class Employee(Person):
    def __init__(self, name, work):
        super().__init__(name)
        self.__work = work



    @property
    def work(self):
        return self.__work

employee_1 = Employee("Arsen","It")
print(employee_1.name)
print(employee_1.work)
person_1 = Person("John")
print(person_1.name)







