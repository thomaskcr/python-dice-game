import random

# Roll the dice and get a number between 1 and 6
dice_number = random.randrange(1, 7)

# Get user's guess from input
print("Guess the number rolled on the six sided dice:")
user_guess = input()

# Convert the user's guess to an integer
user_guess = int(user_guess)
