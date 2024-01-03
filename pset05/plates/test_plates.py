from plates import is_valid


def test_len():
    assert is_valid("A") == False
    assert is_valid("AAAAAAAA") == False
    assert is_valid("AAAA") == True


def test_twoletters():
    assert is_valid("AA") == True
    assert is_valid("12") == False
    assert is_valid("A1") == False
    assert is_valid("2A") == False


def test_isalnum():
    assert is_valid("AA.10") == False


def test_notzero():
    assert is_valid("AA10") == True
    assert is_valid("AA01") == False


def test_ending():
    assert is_valid("AA10A") == False
    assert is_valid("AAA12") == True
