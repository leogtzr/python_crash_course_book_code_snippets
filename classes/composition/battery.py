class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Done! gas tank filled! :)")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # It's own attributes and using a default value.
        # Composition...
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        # To call super's method:
        # super().fill_gas_tank()
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# Notes:

# The super() function at ➍ is a special function that allows you to call a method
# from the parent class. This line tells Python to call the __init__() method from Car,
# which gives an ElectricCar instance all the attributes defined in that method.
# The name super comes from a convention of calling the parent class a superclass and
# the child class a subclass.

my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
