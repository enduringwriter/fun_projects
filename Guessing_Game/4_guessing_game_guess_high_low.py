# Guessing Game
# user has 3 tries to guess a random number between 1 and 10
# continuing code expansion using file version 3a

import random

# variables
play_game = True
attempts = 3
user_guesses_counter = 0


# generate random number
def get_random_number():
    random_number_int = random.randint(1, 10)
    return random_number_int


# Show welcome message to user
print("Welcome to the Guessing Game!")
print("Random number is between 1 and 10.")
print("You have 3 attempts to guess the correct number.")
print("Enter 'q' to quit at anytime.\n")

while play_game:

    # get random number
    random_number = get_random_number()
    print(f"Hint, random number is: {random_number}")

    # user guesses the answer in 3 attempts or game over
    guess = 0
    while guess != random_number:

        # variables
        attempts -= 1  # attempts left

        # get user guess
        choice = input("Enter your guess: ").lower()

        # play or quit game
        if choice == 'q':
            play_game = False
            break
        else:
            guess = int(choice)
            play_game = True

# compare guess with random number
        if guess == random_number:
            print("You guessed correctly!")
            print(f"Total attempts it took to guess the random number: {3 - attempts}\n")
            attempts = 3
            break
        elif attempts == 0:
            print("You lose.\n")
            attempts = 3
            break
        elif guess < random_number:
            print("You guessed too low.")
            print(f"You have {attempts} attempts left. Guess again.")
        elif guess > random_number:
            print("You guessed too high.")
            print(f"You have {attempts} attempts left. Guess again.")
