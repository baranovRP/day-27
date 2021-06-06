# unlimited, unspecified arguments *args
def add(*args):
    print(args)
    sum = 0
    for n in args:
        print(n)
        sum += n
    return sum


# print(add(3, 4, 5))


#
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiplay"]
    print(n)


calculate(2, add=3, multiplay=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-8")
print(my_car.model)
