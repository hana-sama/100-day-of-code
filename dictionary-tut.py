programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])
programming_dictionary["Loop"] = "The action of doing something over and over again."
for k, v in programming_dictionary.items():
    print(k, v)

for key in programming_dictionary.keys():
    print(key)

for value in programming_dictionary.values():
    print(value)