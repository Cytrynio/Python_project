
def loop():
    num = 0
    for i in range(1, 100):
        return num + 1

def fizzbuzz(i):
    try:
        if isinstance(i, (int ,float))and i > 0 :
            if i % 3 == 0 and i % 5 == 0:
                    return 'FizzBuzz'
            elif i % 3 == 0:
                    return "Fizz"
            elif i % 5 == 0:
                    return "Buzz"
            return i
        return None
    except TypeError:
        print("Zły typ danych")

fizzbuzz(loop())