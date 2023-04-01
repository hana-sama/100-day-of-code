#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "hard":
        return HARD_LEVEL_TURNS
    elif level == "easy":
        return EASY_LEVEL_TURNS

def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!\n")
    print("I am thinking of a number between 1 and 100.\n")
    answer = random.randint(1, 100)
    print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    # Repeat the guessing functionality
    while guess != answer:
        # Let the user guess a number
        guess = int(input("Make a guess: "))

        # Check the guess
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()