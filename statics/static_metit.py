#
# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def area(self):
#         return self.x * self.y
#
#
#     @staticmethod
#     def infi(a , b):
#         print("This is static metot")
#         print(a + b)
#
#
#
# #
# #
# # Shape.info(3,4)
# # ob_1 = Shape(1, 2)
# # ob_1.info(3,4)
# # print(ob_1.area)
#
#
#
# class Counter:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         Counter.count += 1
#
#
#
#
#     @staticmethod
#     def get_count_object():
#         print(f" All oblects ={Counter.count}")
#
#
# obj_1 = Counter("ob_1")
# obj_2 = Counter("ob_2")
# Counter_get_count_objects()
# obj_3 = Counter("ob_3")
# Counter.get_count_object()



#
# class Overflow:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self,  other):
#         obj = Overflow(self.value + other.value)
#         return obj
#
#
#     def __iadd__(self, other):
#         self.value += other.value
#         return self
#
#
#
#
#
# ob_1 = Overflow(1)
# ob_2 = Overflow(2)
# ob_3 = ob_1 + ob_2
# ob_1 += ob_2
#
# print(ob_3.value)
# print(ob_1.value)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return self.age > other.age


    def __lt__(self, otherpthon):
        return self.age < other.age

    def info(self):
        return f"{self.name}is {self.age}"

    def __str__(self):
        return f"{self.name}is {self.age}"


Arsen = Person('Arsen', 22)
ali = Person('ali', 15)
print(ali)
print(Arsen)
if Arsen > ali:
    print(True)
    print("Arsen chon")

else:
    print(False)

































































































































































































































































