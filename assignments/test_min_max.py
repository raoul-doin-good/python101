import pytest
from min_max import get_min_value, get_max_value


def test_get_min_value():
    assert get_min_value([]) == None
    assert get_min_value([-13]) == -13
    assert get_min_value([1, -11]) == -11
    assert get_min_value([1, 11]) == 1
    assert get_min_value([1, 11, 1]) == 1
    assert get_min_value([1, -111, 1]) == -111


def test_get_max_value():
    assert get_max_value([]) == None
    assert get_max_value([-13]) == -13
    assert get_max_value([1, -11]) == 1
    assert get_max_value([1, 11]) == 11
    assert get_max_value([1, 12, 1]) == 12
    assert get_max_value([1, 1, 111]) == 111
