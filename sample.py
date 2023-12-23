def get_average():
    with open("data.txt", "r") as data_file:
        data = data_file.readlines()
        data = data[1:]
        refined_data = [float(val.replace("\n", "")) for val in data]
        total = sum(refined_data)
        average = total / len(refined_data)
    return average


result = get_average()


def get_average():
    print("Hi")
    x = "hello"
    
print(get_average())    