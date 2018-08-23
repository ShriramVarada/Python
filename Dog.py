"""Class Dog Description"""


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " is now rolling over")


class Car:
    def __init__(self, make, model, year=2009):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def odometer_reading(self):
        print('The odometer is ' + str(self.odometer))

    def set_odometer(self, number):
        self.odometer=number

    def inc_odometer(self, number):
        if number > 0:
            self.odometer += number
        else:
            print('Enter a positive value')
