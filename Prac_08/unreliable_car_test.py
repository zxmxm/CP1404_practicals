from unreliable_car import UnreliableCar


def main():
    """Test Car"""

    car = UnreliableCar("Prius 1", 100, 50)
    car.drive(60)
    print(car)


main()