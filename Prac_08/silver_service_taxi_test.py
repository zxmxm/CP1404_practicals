from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi"""
    taxi = SilverServiceTaxi("Prius 1", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("Fare: ${:.2f}".format(taxi.get_fare()))


main()