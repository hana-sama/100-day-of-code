# Prompt user for total bill, tip percentage, and number of people
total_bill = float(input("What is the total bill? $"))
tip_percent = float(input("What percentage tip would you like to leave? (10%, 12%, or 15%) "))
num_people = int(input("How many people are splitting the bill? "))

# Calculate tip amount and total amount
if tip_percent == 10:
    tip_amount = total_bill * 0.1
elif tip_percent == 12:
    tip_amount = total_bill * 0.12
else:
    tip_amount = total_bill * 0.15

total_amount = total_bill + tip_amount

# Calculate amount owed per person
per_person = total_amount / num_people

# Print the result
print("Each person should pay: $", round(per_person, 2))
