import pytest

from sort_list import sort_two_elements, sort_list, sort_list2, sort_by_list


def test_sort_two_elements():
    assert sort_two_elements([1, 2]) == [1, 2]
    assert sort_two_elements([2, 2]) == [2, 2]
    assert sort_two_elements([2, 1]) == [1, 2]


def test_sort_list():
    assert sort_list([1, 2]) == [1, 2]
    assert sort_list([2, 2]) == [2, 2]
    assert sort_list([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_sort_list2():
    assert sort_list2([1, 2]) == [1, 2]
    assert sort_list2([2, 2]) == [2, 2]
    assert sort_list2([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_sort_by_list():
    assert sort_by_list([1, 2], [0, 1]) == [1, 2]
    assert sort_by_list([1, 2], [1, 0]) == [2, 1]
    assert sort_by_list([1, 2, 3], [2, 0, 1]) == [2, 3, 1]


def test_sort_by_length():
    assert sort_by_list([1, 2], [0, 1]) == [1, 2]
