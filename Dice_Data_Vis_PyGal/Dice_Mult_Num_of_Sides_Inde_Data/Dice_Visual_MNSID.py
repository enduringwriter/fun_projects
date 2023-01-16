import pygal

from Dice_MNSID import Die


def get_roll_results(num_of_rolls, dice_dictionary):
    """For each roll, sum the die values and return the result as a list."""
    roll_list = []
    for roll in range(num_of_rolls):
        sum_of_each_roll = 0
        for each_die in dice_dict:
            sum_of_each_roll += each_die.get_roll(dice_dictionary[each_die])
        roll_list.append(sum_of_each_roll)
    return roll_list


def get_roll_results_per_die(num_of_rolls, dice_dictionary):
    """Generate a dictionary for each die and its roll result."""
    roll_dict = {}

    for each_die in dice_dict:
        each_die_roll_list = []
        for roll in range(num_of_rolls):
            each_die_rolled = each_die.get_roll(dice_dictionary[each_die])
            each_die_roll_list.append(each_die_rolled)
        roll_dict[each_die] = each_die_roll_list
    return roll_dict


def get_bar_chart(frequencies_gbc, numb_of_dice, numb_of_rolls, dice_dictionary):
    """Generate an SVG chart of Frequencies versus Roll values."""
    bar_chart = pygal.Bar()
    bar_chart.add('Dice', frequencies_gbc)
    bar_chart.x_labels = map(str, range(numb_of_dice, sum(dice_dictionary.values()) + 1))
    bar_chart.title = f"Frequencies of {numb_of_dice} dice rolled {numb_of_rolls} times"
    bar_chart.x_title = "Roll"
    bar_chart.y_title = "Frequency"
    bar_chart.render_to_file("Dice_Frequency_MNSID.svg")


# generate first die inheritance object
die_1 = Die()

# create dice list and get number of dice
dice_list = [die_1]
number_of_dice = Die.get_number_of_dice(die_1)

# generate die inheritance into dice list
for die_number in range(1, number_of_dice):
    dice_list.append(die_number)
    dice_list[die_number] = Die()

# get the number of sides on each die as a dictionary where k:v => die:number of sides
dice_dict = {}
dice_dict = die_1.get_number_of_sides(number_of_dice, dice_list, dice_dict)
print(dice_dict)

# get the number of rolls
number_of_rolls = Die.get_number_of_rolls(die_1)

# # analyze frequencies of all rolls
# frequencies = []
# for x in range(number_of_dice, sum(dice_dict.values()) + 1):
#     frequency = rolls.count(x)
#     frequencies.append(frequency)
# # print(frequencies), print(sum(frequencies))  # verification
#
# # visualize results of frequencies versus rolls
# get_bar_chart(frequencies, number_of_dice, number_of_rolls, dice_dict)

# get the number rolled for each die as a dictionary where k:v => die:[roll result]
roll_dict = get_roll_results_per_die(number_of_rolls, dice_dict)
print("Roll_dict: ", roll_dict)

# sum the dice for each roll as a list
# rolls = list(map(sum, zip(*roll_dict.values())))  # using map and zip
# rolls = [sum(i) for i in zip(*roll_dict.values())]  # using list comprehension and zip
rolls = []  # expanded view of list comprehension and zip
for x in zip(*roll_dict.values()):
    rolls.append(sum(x))
print(rolls)

# analyze the frequency for each possible roll outcome
frequencies = []
for y in range(number_of_dice, sum(dice_dict.values()) + 1):
    frequency = rolls.count(y)
    frequencies.append(frequency)
print("frequencies: ", frequencies), print(sum(frequencies))  # verification

# TODO # calculate the percentage of each die contributing to the total number of frequencies per roll

# TODO - see this tutorial about collections module
# https://codefather.tech/blog/python-count-unique-values-in-list/
# from collections import Counter
# Counter([1,2,3,3])
# Counter({3: 2, 1: 1, 2: 1})
