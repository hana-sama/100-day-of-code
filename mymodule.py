import glob

my_files = glob.glob("files/*.txt")

for filepath in my_files:
    with open(filepath, "a") as local_file:
        local_file.write("Hello, Angela!\n")

    with open(filepath, "r") as local_file:
        content = local_file.read()
        content = content.strip("\n")
        print(content)

import csv

with open("files/weather.csv", "r") as weather_data:
    data = list(csv.reader(weather_data))
    print(data)

import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+")

webbrowser.open(f"https://www.google.com/search?q={user_term}")