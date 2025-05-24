class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "This animal makes a sound"

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Driver(Person):
    def __init__(self, name, age, license_number):
        super().__init__(name, age)
        self.license_number = license_number

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return f"Moving at {self.speed} km/h"

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

class Train(Vehicle):
    pass

class Device:
    def turn_on(self):
        return "Device turned on"

    def turn_off(self):
        return "Device turned off"

class TV(Device):
    pass

class Laptop(Device):
    pass

class Smartphone(Device):
    pass

class ProgrammingLanguage:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello! I am {self.name}."

class Python(ProgrammingLanguage):
    pass

class Java(ProgrammingLanguage):
    pass

class JavaScript(ProgrammingLanguage):
    pass
