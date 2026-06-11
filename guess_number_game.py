# Number Guessing Game 

import random

print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 50
secret_number = random.randint(1, 50)

attempts = 0
guess = 0


while guess != secret_number:
    guess = int(input("Enter your guess (1-50): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")

print("It took you", attempts, "attempts.")
