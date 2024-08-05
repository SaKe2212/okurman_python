class Book:
    def __init__(self, title, author):
     self.title = title,
     self.__author = author

    def get_title(self):
        return self.title


    def get_author(self):
        return self.__author

    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author):
        self.__author= author


Book_1 = Book("Pyton",  "User")
print(Book_1.title)
Book_1.title = "java"
print(Book_1.title)
print(Book_1.author)
Book_1.author = "Person"
print(Book_1.author)


class Person:
    def __init__(self, name, age):
        self.name = name,
        self.age = age

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age):
        self.age = age
        if age < 0:
            print("Sorry, The age cannot be negative")


person_1= Person("John", 25)
print(person_1.age)
person_1.age = 22
print(person_1.age)



class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.__colour = colour

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        if colour in ('Blue', 'Black', 'White'):
            self.__colour = colour


        else:
            print("Sorry, the colour must be blue, black, white")
            print(f"The dog colour cant be {colour}")


dog_1 = Dog("John", 25, "Blue")
print(dog_1.colour)
dog_1.colour = "Black"
print(dog_1.colour)





