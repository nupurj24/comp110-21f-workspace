"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730391424"


def test_only_evens_empty() -> None:
    """Should return an empty list if given an empty list."""
    input_list: list[int] = []
    assert only_evens(input_list) == []


def test_only_evens_only_odds() -> None:
    """Given only odds, the function should return an empty list."""
    input_list: list[int] = [1, 3, 5, 7]
    assert only_evens(input_list) == []


def test_only_evens_negatives() -> None:
    """Given negatives, the function should still return which ones are even."""
    input_list: list[int] = [-1, -4, -2, 6, 5, 8]
    assert only_evens(input_list) == [-4, -2, 6, 8]


def test_sub_start_bigger_than_list() -> None:
    """Given a start index that is larger than the length of the list should return an empty list."""
    a_list: list[int] = [1, 2, 3, 4]
    start: int = 6
    end: int = 7
    assert sub(a_list, start, end) == []


def test_sub_start_is_negative() -> None:
    """Given a negative value for start, the subset should start from the value at the first index."""
    a_list: list[int] = [1, 2, 3, 4]
    start: int = -2
    end: int = 2
    assert sub(a_list, start, end) == [1, 2]


def test_sub_end_is_greater_than_length_of_list() -> None:
    """Given an end value that is larger than the length of the list, the returned subset should end with the last value of the list."""
    a_list: list[int] = [1, 2, 3, 4]
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == [2, 3]


def test_concat_lists_are_empty() -> None:
    """Given two empty lists, the function should return an empty list."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_first_list_is_shorter() -> None:
    """Given a first list that is shorter than the second, the function should still concatenate."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6, 7]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7]


def test_concat_first_list_is_longer() -> None:
    """Given a first list that is longer than the second, the function should still concatenate."""
    list_1: list[int] = [1, 2, 3, 4, 5]
    list_2: list[int] = [6, 7]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7]