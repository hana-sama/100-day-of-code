import json
import time
print(time.strftime("%A"))

# Read data from json file
with open("quiz.json", "r") as quiz_file:
    data = quiz_file.read()

# Create list from retrieved json data
content = json.loads(data)
print(content)
index = 0
score = 0
while index < len(content):
    print(content[index]["question_text"])
    for key, answer in enumerate(content[index]["alternatives"]):
        print(f"{key + 1}-{answer}")
    user_choice = int(input("Please select from the above: "))
    if user_choice == content[index]["correct_answer"]:
        print("You've got it right.")
        score += 1
    else:
        print("Wrong anser")
    print(f"Current score: {score}/{index}")
    index += 1
    