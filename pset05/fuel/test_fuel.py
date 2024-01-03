from fuel import convert, gauge
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error1():
    with pytest.raises(ValueError):
        convert("5/4")


def test_value_error2():
    with pytest.raises(ValueError):
        convert("cat")


def test_attribute_error():
    with pytest.raises(AttributeError):
        convert(1)


def test_convert():
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
