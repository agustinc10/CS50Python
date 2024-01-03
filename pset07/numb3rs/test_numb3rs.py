from numb3rs import validate


def test_1():
    assert validate("0") == False
    assert validate("255") == False


def test_2():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("256.256.256.256") == False


def test_3():
    assert validate("0.256.256.256") == False
