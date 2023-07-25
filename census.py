import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_counts = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_counts = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_counts = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_counts)
print(red_squirrels_counts)
print(black_squirrels_counts)

squirrel_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_counts, red_squirrels_counts, black_squirrels_counts]
}

df = pandas.DataFrame(squirrel_data)
df.to_csv("squirrel_count.csv")

squirrel_count_data = pandas.read_csv("squirrel_count.csv")
print(squirrel_count_data)