import random as rd

def guessing_number(com_num, attempts):
  for i in range(attempts, 0, -1):
    try:
      guess_name = int(input("Enter the Number: "))
      if guess_name > com_num: print("Too high!") # if the guess is greater than the number.
      if guess_name < com_num: print("Too low!") # if the guess is less than the number.
      if guess_name == com_num: # if the guess matches the number.
        print(f"Congratulations! You guessed the number {com_num} correctly!")
        break
      if i == 1: # if the user runs out of attempts
        print(f"Sorry, you've run out of attempts. The correct number was {com_num}.")
        break
      print(f"Attempts left: {i-1}\n")
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue


def user_attempts(diff_lvl):
  attempts = {
      "1": 10,
      "2": 5,
      "3": 3
  }.get(diff_lvl, 10)  # Default to 10 if invalid

  if diff_lvl not in ["1", "2", "3"]:
    print("Invalid input. Defaulting to Easy (10 attempts).")

  return attempts


def game():
  print("======================================")
  print(" Welcome to the Number Guessing Game! ")
  print("======================================\n")

  print("1. Easy (10 attempts)")
  print("2. Medium (5 attempts)")
  print("3. Hard (3 attempts)")

  # The user selects the difficulty level.
  diff_lvl = input("Select the difficulty level: ")
  attempts = user_attempts(diff_lvl)

  # The computer randomly picks a number within a range (e.g., 1 to 100).
  com_num = rd.randint(1, 100)
    
  print("\nThe computer has selected a number between 1 and 100.")
  print("You can enter 'exit' to quit the game at any time.\n")

  guessing_number(com_num, attempts)

 
def main():
  try:
    game()

    while(True):
      play_again = input("\nWant to play again? (y/n): ")
      try:
        if play_again == "y":
          game()
        elif play_again == "n":
          print("Thanks for playing!")
          break
        else:
          print("Invalid input. Please enter 'y' or 'n'.")
      except ValueError:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
  except KeyboardInterrupt:
    print("\nProgram interrupted by user (Ctrl+C)")

main()

# 🎯 Game Rules (for a basic version):
# The computer randomly picks a number within a range (e.g., 1 to 100).

# The player tries to guess the number.

# After each guess, the program tells the player:

# "Too high!" if the guess is greater than the number.

# "Too low!" if the guess is less than the number.

# "Correct!" if the guess matches the number.

# The game ends when the player guesses correctly.

# (Optional) Show the number of attempts.

# 🛠️ What You Should Implement:
# Import the random module.

# Use random.randint(a, b) to generate a secret number.

# Use a while loop to keep asking for guesses.

# Use input() to get user input and convert to int.

# Add logic to compare guess with the secret number.

# (Optional) Track the number of attempts and display it.

# 💡 Optional Features to Level It Up:
# Add a maximum number of attempts.

# Let the player choose the difficulty (easy, medium, hard).

# Ask if they want to play again after winning.

# Add error handling (e.g., user types letters instead of numbers).