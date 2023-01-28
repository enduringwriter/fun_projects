# Guessing Game
# user has 3 tries to guess a random number between 1 and 10

import random

# variables
attempts = 3
user_guesses_counter = 0


# generate random number
def get_random_number():
    random_number_int = random.randint(1, 10)
    return random_number_int


# Show welcome message to user
print("Welcome to the Guessing Game!")
print("Random number is between 1 and 10.")
print("You have 3 attempts to guess the correct number.\n")

# get random number
random_number = get_random_number()
print(f"Hint, random number is: {random_number}")

# user guesses the answer in 3 attempts or game over
while attempts != 0:

    # variables
    user_guesses_counter += 1  # count user guesses
    attempts -= 1  # attempts left

    # get user guess
    guess = int(input("Enter your guess: "))

    # compare user guess with random number
    if guess == random_number:
        print("You guessed correctly!")
        print(f"Total attempts it took to guess the random number: {user_guesses_counter}")
        break
    elif attempts == 0:
        print("You lose.")
    else:
        print(f"You have {attempts} attempts left. Guess again.")
