import random

def guessing_game():
    """
    Plays a number guessing game where the user guesses a number between 1 and 10.
    """
    secret_number = random.randint(1, 10)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 10:
                print("Please guess a number within the range of 1 to 10.")
            elif user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guessing_game()