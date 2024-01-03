from um import count

def test_1():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("Um") == 1


def test_2():
    assert count("hum") == 0
    assert count("umbrella") == 0


def test_3():
    assert count("Um, thanks, um , for the album...") == 2
