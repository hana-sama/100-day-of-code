with open("/home/hana/tutorials/100-day-of-python/day-24/my_file.txt", mode="w") as file:
    file.write("Hello, my name is Angela.")

with open("/home/hana/tutorials/100-day-of-python/day-24/my_file.txt", mode="a") as file_2:
    file_2.write("\nI am 12 years old.")

with open("/home/hana/tutorials/100-day-of-python/day-24/my_file.txt", mode="a") as file_3:
    file_3.write("\nMy favorite food is a bowl of hot nooeldes.")

with open("/home/hana/tutorials/100-day-of-python/day-24/my_file.txt") as f:
    contents = f.read()
    print(contents)


with open("../../../hana/my_file.txt", "w") as file:
    file.write("Hello, my name is Angela.")

with open("../../../hana/my_file.txt", "r") as file:
    content = file.read()
    print(content)