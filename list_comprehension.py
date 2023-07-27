numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:

print(result)


name = "Angela"
name_list = [letter for letter in name]
print(name_list)

# Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie", "Angela"]


short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_long_names = [name.upper() for name in names if len(name) > 5]
print(upper_long_names)