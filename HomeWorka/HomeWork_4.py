class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name}")

    def eat(self):
        print(f"{self.name}")
my_dog = Dog("Барбос", 3)
my_dog.sleep()
my_dog.eat()
