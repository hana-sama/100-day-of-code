def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

result = add(3, 4, 6, 8, 10, 101)
print(result)

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, mutiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get('seats')

my_car = Car(make="Nissan")
print(my_car.model)

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)