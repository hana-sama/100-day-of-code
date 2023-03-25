import os
from art import logo

print(logo)
print("Welcome to the secret auction program")


bids = {}
is_auction_over = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not is_auction_over:
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[bidder] = bid
    should_continue = input("Are there any more bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "yes":
        os.system('clear')
    elif should_continue == "no":
        is_auction_over = True
        # winning_bid = max(bids.values())
        # winner = list(bids.keys())[list(bids.values()).index(winning_bid)]
        find_highest_bidder(bids)
        print("Thank you for using our wonderful auction app!")
