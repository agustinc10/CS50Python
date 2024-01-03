from seasons import calculate_time
from datetime import date, timedelta
import pytest


def test_1():
    today = date.today()
    assert (
        calculate_time(str(date(today.year - 1, today.month, today.day)))
        == "Five hundred twenty-five thousand, six hundred minutes"
    )
    assert (
        calculate_time(str(date(today.year - 2, today.month, today.day)))
        == "One million, fifty-one thousand, two hundred minutes"
    )


def test_2():
    with pytest.raises(SystemExit):
        calculate_time("1945")


def test_3():
    try:
        calculate_time("January 5")
        assert False, "Expected SystemExit"
    except SystemExit:
        pass
