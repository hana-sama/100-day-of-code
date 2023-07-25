import pandas as pd

df = pd.read_csv("weather_data.csv")
print(type(df))
print(df.to_dict())

temp_series = df["temp"]
temp_list = df["temp"].to_list()
print(type(temp_series))

average = temp_series.mean()
print(f"{average:.1f}")
max_temp = temp_series.max()
print(f"{max_temp:.1f}")

# Get data in row
print(df[df.day == "Monday"])
print(df[df.temp == df.temp.max()])

monday = df[df.day == "Monday"]
print(monday.condition)
temp_in_fehrenheit = (int(monday.temp) * (9/5)) + 32
print(temp_in_fehrenheit)

# Create a dataframe from scrath
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
# import csv
# with open("/home/hana/tutorials/100-day-of-python/day-25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#     for temp in temperatures:
#         print(temp)