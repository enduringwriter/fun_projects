import random


class Die():
    """Create a class."""
    def __init__(self, number_of_dice=1, number_of_sides=6, number_of_rolls=100):
        """Create instance attributes."""
        self.number_of_sides = number_of_sides
        self.number_of_rolls = number_of_rolls
        self.number_of_dice = number_of_dice

    def get_number_of_dice(self):
        """Get the total number of dice to roll with."""
        number_of_dice = int(input("Enter the number of dice to roll with: "))
        return number_of_dice

    def get_number_of_sides_of_die(self):
        """Get the total number of sides of the die."""
        number_of_sides = int(input("Enter the number of sides on the dice: "))
        return number_of_sides

    def get_number_of_rolls(self):
        """Get the total times the die or dice will be rolled."""
        total_to_roll = int(input("Enter the number of times to roll the dice together: "))
        return total_to_roll

    def get_roll(self, number_of_sides):
        """Generate a random roll."""
        return random.randint(1, number_of_sides)
