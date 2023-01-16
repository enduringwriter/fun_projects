import random


class Die():
    """Create a class."""
    def __init__(self, number_of_dice=1, number_of_sides=6, number_of_rolls=100):
        """Create instance attributes."""
        self.number_of_dice = number_of_dice
        self.number_of_sides = number_of_sides
        self.number_of_rolls = number_of_rolls

    def get_number_of_dice(self):
        """Get the total number of dice to roll with."""
        number_of_dice = int(input("Enter the number of dice to roll with: "))
        return number_of_dice

    def get_number_of_sides(self, number_of_dice, dice_list, dice_dict):
        """Get the total number of sides of the die."""
        for item in dice_list:
            number_of_sides = int(input(f"Enter the number of sides on die {number_of_dice}: "))
            dice_dict[item] = number_of_sides
            number_of_dice -= 1
        return dice_dict

    def get_number_of_rolls(self):
        """Get the total times the die or dice will be rolled."""
        number_of_rolls = int(input("Enter the number of times to roll the dice together: "))
        return number_of_rolls

    def get_roll(self, number_of_sides):
        """Generate a random roll."""
        return random.randint(1, number_of_sides)
