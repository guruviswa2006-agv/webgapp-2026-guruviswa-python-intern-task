from abc import ABC
class Vehicle(ABC):
    def start(self):
        pass
class Bike(Vehicle):
    def start(self):
        print("Bike Started")
class Car(Vehicle):
    def start(self):
        print("Car started")
b=Bike()
b.start()
c=Car()
c.start()