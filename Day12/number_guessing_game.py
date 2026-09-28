import random


def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        if difficulty == "hard":
            return 5
        print("Please type 'easy' or 'hard'.")


def get_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 1 <= guess <= 100:
            return guess
        print("Please enter a number between 1 and 100.")


def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    attempts = choose_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = get_guess()

        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            break

        if guess < answer:
            print("Too low.")
        else:
            print("Too high.")

        attempts -= 1
        if attempts > 0:
            print("Guess again.")
    else:
        print(f"You ran out of guesses. The correct answer was {answer}.")

    print("Thank you for playing the game!")


play_game()
