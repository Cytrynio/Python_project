from multiply.main import multiply

def test_multiply_integer():
    assert multiply(2,5) == 10
    assert multiply(2, 1) == 2
    assert multiply(5, 4) == 20
    assert multiply(3, 7) == 21

def test_multiply_float():
    assert multiply(100, 1.1) == 110
    assert  multiply(5, 3.5) == 17.5

def test_multiply_small():
    assert multiply(0.01, 0.03) == 0.0003

def test_multiply_string():
    assert multiply('5','3') == 15

def test_multiply_string_not_to_int():
    assert multiply('4', 'ala') is None
