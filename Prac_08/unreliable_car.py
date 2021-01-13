from car import Car
import random


class UnreliableCar(Car):
    """Unreliable Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Test car, based on reliability"""
        number = random.randint(1, 100)
        print(number)
        if number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

