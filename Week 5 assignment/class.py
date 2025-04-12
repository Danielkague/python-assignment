# Defining a class
class Bike:
    color = "black"  # Attribute

    # Method
    def ride(self):
        print("Riding My Bike")

# Creating an object
my_bike = Bike()
print(my_bike.color)
my_bike.ride()


class Bike:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
bike1 = Bike("black", "Ducati")
bike2 = Bike("yellow", "Kawasaki")

print(bike1.color)  # Output: black
print(bike1.model)  # Output: Ducati
print(bike2.color)  # Output: yellow
print(bike2.model)  # Output: Kawasaki


class Motorcycle:
    def __init__(self, wheels):
        self.wheels = wheels

class Bike(Motorcycle):
    pass

Bike = Bike(2)
print(Bike.wheels)  # Output: 2