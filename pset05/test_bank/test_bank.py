from bank import value

def test_100():
    assert value("Yey") == 100
    assert value("yey") == 100
    assert value(".hey") == 100

def test_20():
    assert value("hey") == 20
    assert value("Hi") == 20
    assert value("h") == 20

def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0
