import random
import logo_art

Easy_Level_Attempts = 15
Hard_Level_Attempts = 5

def set_difficulty(levelchose):
    if levelchose == "easy":
        return Easy_Level_Attempts
    elif levelchose == "hard":
        return Hard_Level_Attempts
    else:
        return None

def check_the_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high")
        return attempts - 1
    else:
        print(f" Your Guess is Right! The Answer was {answer}")
        return attempts

def game():
    print(logo_art.logo)
    print("Let me think of a number between 1 to 50.")
    answer = random.randint(1, 50)

    level = input("Choose level of difficulty...Type 'easy' or 'hard': ").lower()
    attempts = set_difficulty(level)

    if attempts is None:
        print("You have entered wrong difficulty level...Play again!!")
        return

    guessed_number = 0
    while guessed_number != answer and attempts > 0:
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Guess a number: "))

        attempts = check_the_answer(guessed_number, answer, attempts)

        if guessed_number != answer and attempts > 0:
            print("Guess again.")

        if attempts == 0 and guessed_number != answer:
            print(f"You are out of guesses... You lose! The number was {answer}")

game()
