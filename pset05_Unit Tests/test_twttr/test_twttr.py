from twttr import shorten

def test_caps():
    assert shorten("AEIOU") == ""


def test_lower():
    assert shorten("aeiou") == ""


def test_consonants():
    assert shorten("BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz") == "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"


def test_numbers():
    assert shorten("CS50") == "CS50"


def test_punctuation():
    assert shorten("C.S_5,0:") == "C.S_5,0:"
