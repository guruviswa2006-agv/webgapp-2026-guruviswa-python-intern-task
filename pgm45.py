class Car:
    wheels = 4
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    def drive(self):
        return f'{self.brand} is driving!'
car1 = Car('Toyota', 'Red')
car2 = Car('Honda', 'Blue')
print(car1.drive())
print(car2.brand)
print(Car.wheels)