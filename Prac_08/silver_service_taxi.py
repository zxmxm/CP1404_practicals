from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised a SilverServiceTaxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus flagfall of ${:.2f}/km".format(super().__str__(),
                                                       self.flagfall)

    def get_fare(self):
        """Get the fare"""
        fare = round(self.flagfall + super().get_fare())
        return fare

