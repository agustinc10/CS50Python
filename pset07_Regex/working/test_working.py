from working import convert


def test_1():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:30 PM") == "00:30 to 12:30"
    assert convert("1 AM to 11 PM") == "01:00 to 23:00"
    assert convert("1:00 AM to 11:00 PM") == "01:00 to 23:00"
    assert convert("11 AM to 1 PM") == "11:00 to 13:00"
    assert convert("11:00 AM to 1:00 PM") == "11:00 to 13:00"


def test_2():
    try:
        convert("11 AM 1 PM")
        assert False, "Expected ValueError"
    except ValueError:
        pass


def test_3():
    try:
        convert("12:65 AM to 13:70 PM")
        assert False, "Expected ValueError"
    except ValueError:
        pass
