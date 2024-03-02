class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def get_name(self):
        return f'Your name is {self.name.capitalize()}'

    def age(self, current_year):
        return f'Hi {self.name}. Your age is {current_year - self.birthday} years old'
    

john = User(name="angela", birthday=1999)

print(john.get_name())
print(john.age(current_year=2024))