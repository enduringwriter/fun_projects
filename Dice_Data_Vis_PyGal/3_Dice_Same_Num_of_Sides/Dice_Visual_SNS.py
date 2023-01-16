import pygal

from Dice_SNS import Die

# generate first die inheritance object, default of program
die_1 = Die()

# generate dice list and add first die
dice_list = [die_1]

# get number of dice
number_of_dice = die_1.get_number_of_dice()

# if there are 2 or more dice
if number_of_dice > 1:
    for x in range(1, number_of_dice):
        dice_list.append(x)
        dice_list[x] = Die()

    # unused and incomplete nomenclature for die inheritance, best to use a dictionary
    # for item in range(1, num_of_dice):
    #     y = 'dice_' + str(item)

# get number of sides and number of rolls
number_of_sides = die_1.get_number_of_sides_of_die()
number_of_rolls = die_1.get_number_of_rolls()

# generate roll results
rolls = []
for roll_num in range(number_of_rolls):
    sum_of_each_roll = 0
    for die_num in dice_list:
        sum_of_each_roll += die_num.get_roll(number_of_sides)
    rolls.append(sum_of_each_roll)

print(rolls)

# analyze frequencies of all rolls
frequencies = []
for x in range(number_of_dice, number_of_dice * number_of_sides + 1):
    frequency = rolls.count(x)
    frequencies.append(frequency)

print(frequencies)
print(sum(frequencies))  # verification

# if wanting to convert integer into word for visualization, use code or import a module
# https://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words

# visualize results of frequencies versus rolls
bar_chart = pygal.Bar()
bar_chart.add(f"{number_of_sides}D", frequencies)
bar_chart.x_labels = map(str, range(number_of_dice, number_of_dice * number_of_sides + 1))
bar_chart.title = f"Frequencies of {number_of_dice} {number_of_sides}-sided dice rolled {number_of_rolls} times"
bar_chart.x_title = "Roll"
bar_chart.y_title = "Frequency"

bar_chart.render_to_file('Dice_Frequency_SNS.svg')
