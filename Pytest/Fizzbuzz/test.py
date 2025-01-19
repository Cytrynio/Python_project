from main import fizzbuzz


def test_fizz_number():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"

def test_fizz_buzz_exceptions():
    assert fizzbuzz('Dupa') is None
    assert fizzbuzz(-4) is None
