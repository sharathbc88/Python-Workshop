from Practical08.taxi import Taxi, UnreliableCar

limo1 = Taxi("Limo 1", 100, 2)
limo1.drive(40)
limo1.start_fare()
limo1.drive(100)
print(limo1)

lousy_car = UnreliableCar(100, 50)
print(lousy_car)
lousy_car.drive(50)
print(lousy_car)

