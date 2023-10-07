import random

def guess_game():
  """Guesses a random number between 0 and 100 in 5 attempts, ignoring non-integer inputs and finishing the game when the player wins or loses."""

  # Generate a random number between 0 and 100.
  secret_number = random.randint(0, 100)

  # Initialize the number of guesses and the game over flag.
  num_guesses = 0
  game_over = False

  # Start the guessing loop.
  while num_guesses < 5 and not game_over:
    # Get the player's guess.
    try:
      guess = int(input("Guess a number between 0 and 100: "))
    except ValueError:
      # Ignore the input if it is not an integer.
      continue

    # Check if the guess is correct.
    if guess == secret_number:
      print("Congratulations! You guessed the correct number!")
      game_over = True
    else:
      # Tell the player if their guess is too high or too low.
      if guess > secret_number:
        print("Your guess is too high.")
      else:
        print("Your guess is too low.")

      # Increment the number of guesses.
      num_guesses += 1

  # If the player reaches here, it means they have run out of guesses or they have won the game.
  if game_over:
    print("You win!")
  else:
    print(f"Sorry, you ran out of guesses. The correct number was {secret_number}.")
  # Ask the player if they want to play again.
  play_again = input("Do you want to play again? (y/n) ")

  # Return True if the player wants to play again, False otherwise.
  return play_again == "y"

guess_game()