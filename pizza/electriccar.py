# from Dog import Car, Dog
import Dog


class Battery:
    def __init__(self, battery_size=56):
        self.battery_size = battery_size

    def battery_lifepercent(self):
        return self.battery_size*2/100

    def range(self):
        global range2
        if self.battery_size > 80:
            range2 = 30
        elif self.battery_size < 80:
            range2 = 20

        message=''
        message += "This car goes approx 90 miles /h"
        print(message)
        return range2


class ElectricCar(Dog.Car):
    def __init__(self, make, model, year=3):
        """Need a default parameter in the subclass constructor"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery.battery_size) + "-kWh battery. And life "
                                                                   "percent is " +
              str(self.battery.battery_lifepercent()) + " and the range is " + str(self.battery.range()))

    def inc_odometer(self, number):
        self.odometer += number*2


car = ElectricCar('da', 'das', 43)
car.inc_odometer(2)
car.odometer_reading()
car.describe_battery()

d = Dog.Dog('ads', 45)
print(d.age)
ds = Dog.Car('as', 'Bn')
print(ds.get_descriptive_name())