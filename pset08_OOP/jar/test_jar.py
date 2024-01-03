from CS50Python.pset08.jar.jar import Jar


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    try:
        jar.deposit(15)
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    try:
        jar.withdraw(15)
        assert False, "Expected ValueError"
    except ValueError:
        pass
