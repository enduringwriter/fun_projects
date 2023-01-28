# Guessing Game
# user has one try to guess a random number between 1 and 10

import random

# Show welcome message to user
print("Welcome to the Guessing Game!")
print("Random number is between 1 and 10\n")

# generate random number
random_number = random_number_int = random.randint(1, 10)
print(f"Hint, random number is: {random_number}")

# get user guess
guess = int(input("Enter your guess: "))

# compare user guess with random number
if guess == random_number:
    print("You guessed correctly!")
else:
    print("You lose.")
