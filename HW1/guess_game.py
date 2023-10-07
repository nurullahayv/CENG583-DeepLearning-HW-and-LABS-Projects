import random

def guess_game():
    secret_number = 5 #random.randint(0, 100)
    attempts = 5

    print("Welcome to the Guessing Game!")
    print("You have 5 attempts to guess the number between 0 and 100.")

    for attempt in range(1, attempts+1):
        guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You've guessed the number ({secret_number}) correctly!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

# Run the game
guess_game()