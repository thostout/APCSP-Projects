# Loops Program #2: Guessing Game
# A simple guessing game where the user has to guess a randomly generated number
# Thomas Stout
# 1/12/26

import random

num = random.randint(1, 100)
num_guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess < num:
        print("Too low! Try again.")
        num_guesses += 1
    elif guess > num:
        print("Too high! Try again.")
        num_guesses += 1
    else:
        num_guesses += 1
        print(f"You've guessed the correct number. It took you {num_guesses} guesses.")
        break
