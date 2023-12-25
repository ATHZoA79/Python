class Vehicle:
    # define a class variable
    # child lass will automatically inherite class variable
    # VALUE CANNOT Be CHANGE
    color = 'White'

    def __init__(self, name, max_speed, mileage):
        # These are called instance variables
        # VALUE IS MODIFIED BY ARGUMENT
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass