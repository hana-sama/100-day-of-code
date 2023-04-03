from art import logo
from art import vs
from game_data import data
import random
import os
score = 0


def format_data(account):
    """Takes the account data and return printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_descr}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if user is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display logo
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make the game repeatble
while game_should_continue:
    # Generate random account from game data

    # Make account at position b become the next account at position a
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask user to guess which account has higher followers
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen
    os.system("clear") 
    print(logo)
    # Give the user some feedback
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
    # print(a_follower_count, b_follower_count)