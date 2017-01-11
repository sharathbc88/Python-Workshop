"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Practical07.car import Car

def assign():
    limo = Car("limo",100)
    limo.add_fuel(20)
    print(limo.fuel)

    limo.drive(115)
    print(limo.odometer)

    limo.fuel =42
    limo.odometer =115
    print(limo)
assign()

def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))

