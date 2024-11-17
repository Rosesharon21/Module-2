import random

# Step 2: Initialize number_to_guess
number_to_guess = random.randint(1, 100)

# Step 3: Initialize guess
guess = None

# Step 4: Loop until the correct guess
while guess != number_to_guess:
    # Step 4.1: Prompt player to enter a guess
    guess = int(input("Enter your guess (between 1 and 100): "))
    
    # Step 4.3: Check if the guess is too low
    if guess < number_to_guess:
        print("Too low!")
    # Step 4.4: Check if the guess is too high
    elif guess > number_to_guess:
        print("Too high!")
    # Step 4.5: Correct guess
    else:
        print("Congratulations! You've guessed the correct number!")

# Step 5: End
