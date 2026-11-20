from integer_jenkins import check_even_odd
def test_check_even_odd():
    assert check_even_odd(10) == "Even"
def test_check_even_odd_odd():
    assert check_even_odd(9) == "Odd"
def test_check_even_odd_zero():
    assert check_even_odd(0) == "Even"