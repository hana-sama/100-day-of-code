import csv

with open("data.csv", newline="") as data_file:
    spamreader = csv.reader(data_file, delimiter=" ", quotechar="|")
    for row in spamreader:
        print(" ".join(row))
