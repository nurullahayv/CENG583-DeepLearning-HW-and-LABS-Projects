import random

def guess_game():
  """Guesses a random number between 0 and 100 in 5 attempts."""

  game_over = False
  # Generate a random number between 0 and 100.
  number = 5#random.randint(0, 100)

  # Initialize the number of guesses.
  playername = str(input("What is your name: "))
  num_guesses = 0

  # Start the guessing loop.
  while num_guesses < 5:
    # Get the player's guess.

    if num_guesses == 0 :
        try:
          guess = int(input(f" Hi, {playername} please guess a number between 0 and 100: "))
        except ValueError:
            continue
    else:
        try:
          guess = int(input(f" {playername} please guess a number between 0 and 100: "))
        except ValueError:
          continue

    # Check if the guess is correct.
    if guess == number:
      print("Congratulations! You guessed the correct number!")
      return True
    else:
      # Tell the player if their guess is too high or too low.
      if guess > number:
        print("Your guess is too high.")
      else:
        print("Your guess is too low.")

      # Increment the number of guesses.
      num_guesses += 1

  # If the player reaches here, it means they have run out of guesses.
  print(f"Sorry, you ran out of guesses. The correct number was {number}.")
  
  return False


# Play the game.
if __name__ == "__main__":
  if guess_game():
    print("You win!")
  else:
    print("You lose.")
    
    
guess_game()
