import random


class Die:
    """Create a class representing a single die."""

    def __init__(self, number_of_sides=6, number_of_rolls=100):
        """Create instance attributes."""
        self.number_of_sides = number_of_sides
        self.number_of_rolls = number_of_rolls

    def get_roll(self):
        """Generate a random roll."""
        # python range function is up to but not including the final number
        # randint function includes the final number
        return random.randint(1, self.number_of_sides)
