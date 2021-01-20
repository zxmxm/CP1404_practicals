from taxi import Taxi


def main():
    """Test Taxi"""

    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print("Fare: ${:.2f}".format(taxi.get_fare()))

    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print("Fare: ${:.2f}".format(taxi.get_fare()))


main()
