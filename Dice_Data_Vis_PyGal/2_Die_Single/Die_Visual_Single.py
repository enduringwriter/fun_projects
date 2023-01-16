import pygal

from Die_Single import Die

# generate first die inheritance object, default of program
die = Die()

# get number of sides and number of rolls
number_of_sides = die.get_num_of_sides_of_die()
number_of_rolls = die.get_num_of_rolls()

# generate roll results
rolls = []
for x in range(number_of_rolls):
    result = die.get_roll(number_of_sides)
    rolls.append(result)

print(rolls)

# analyze frequencies of all rolls
frequencies = []
for x in range(1, number_of_sides + 1):
    frequency = rolls.count(x)
    frequencies.append(frequency)

print(frequencies)
print(sum(frequencies))  # verification

# visualize results of frequencies versus rolls
bar_chart = pygal.Bar()
bar_chart.add('6D', frequencies)
bar_chart.x_labels = map(str, range(1, number_of_sides + 1))
bar_chart.title = f"Frequencies of a {number_of_sides}-sided die rolled {number_of_rolls} times"
bar_chart.x_title = "Roll"
bar_chart.y_title = "Frequency"

bar_chart.render_to_file('Die_Frequency_Single.svg')
