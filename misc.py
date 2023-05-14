# Polymorphism
# Encapsulation
# Inheritance

from abc import ABC, abstractmethod


class Animal(ABC):
    name = "Barsique"

    def __init__(self, animal_type, size):
        self.type = animal_type
        self.size = size

    @abstractmethod
    def speak(self):
        """This is my docstring"""

    def walk(self):
        return "walking"


class Dog(Animal):
    def __init__(self, animal_type, size, owner):
        super().__init__(animal_type, size)
        self.owner = owner

    def __return_woof(self):
        return "woof"

    def speak(self):
        return self.__return_woof()


class Cat(Animal):
    def speak(self):
        return "meow"


dogs = [Dog("mammal", "smol", "john scatman") for i in range(100)]

cats = [Cat("mammal", "very big chonky cat") for k in range(200)]

animals = dogs + cats

my_lovely_cat = Cat("semka", "big_fluffy_and nice")

my_lovely_cat.speak()

# for animal in animals:
#     if isinstance(animal, Dog):
#         print(animal.owner)
#     print(animal.type)
#     print(animal.speak())

print(issubclass(Animal, object))


def wrapper_function():

    def other_inner_func():
        return 200

    def inner_function(a, b):
        return a + b

    return inner_function
