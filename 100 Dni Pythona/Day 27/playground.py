def add(*args):
    result = 0
    for num in args:
        result += num
    return result


print(add(1,2,3))


def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    #
    # print(kwargs["add"])
    n+= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2,add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GTR")
print(my_car.make)