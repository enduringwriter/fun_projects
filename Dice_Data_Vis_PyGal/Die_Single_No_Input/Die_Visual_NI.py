import pygal

from Die_Single_NI import Die

# generate first die inheritance object from Die class
# a six-sided die is also known as D6
die = Die()

# generate roll results
rolls = []
for roll_num in range(die.number_of_rolls):
    result = Die.get_roll(die)
    rolls.append(result)

print(rolls)

# analyze frequencies of all rolls
frequencies = []
for value in range(1, die.number_of_sides+1):
    frequency = rolls.count(value)
    frequencies.append(frequency)

print(frequencies)

# visualize results of frequencies versus rolls
bar_chart = pygal.Bar()
bar_chart.add('6D', frequencies)
bar_chart.x_labels = map(str, range(1, die.number_of_sides + 1))
bar_chart.title = f"6-Sided Die Frequencies, {die.number_of_rolls} Random Rolls"
bar_chart.x_title = "Number on Die"
bar_chart.y_title = "Frequency"

bar_chart.render_to_file('Die_Frequency_Single_NI.svg')
