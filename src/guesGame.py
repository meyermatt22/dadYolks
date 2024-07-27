import random

def play_game():

    lower_bound = 1
    upper_bound = 100

    number_to_guess = random.randint(lower_bound, upper_bound)

    print(f"Guess the number between {lower_bound} and {upper_bound}!")

    guess = None
    attempts = 0


    while guess != number_to_guess:
        try:

            guess = int(input("Enter your guess: "))

            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number between {lower_bound} and {upper_bound}.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:

            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        play_game()

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
