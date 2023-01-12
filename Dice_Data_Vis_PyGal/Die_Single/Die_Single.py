import random


class Die():
    """Create a class representing a single die."""
    def __init__(self, number_of_sides=6, number_of_rolls=100):
        """Create instance attributes."""
        self.number_of_sides = number_of_sides
        self.number_of_rolls = number_of_rolls

    def get_num_of_sides_of_die(self):
        """Get the total number of sides on the die."""
        number_of_sides = int(input("Enter number of sides of the die: "))
        return number_of_sides

    def get_num_of_rolls(self):
        """Get the total times the die will be rolled."""
        total_to_roll = int(input("Enter number of times to roll the die: "))
        return total_to_roll

    def get_roll(self, number_of_sides):
        """Generate a random roll."""
        # python range function is up to but not including the final number
        # randint function includes the final number
        return random.randint(1, number_of_sides)
