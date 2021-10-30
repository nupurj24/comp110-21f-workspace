"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest 
__author__ = "730391424"


def test_invert_multiple_keys() -> None:
    """Raise Error."""
    with pytest.raises(KeyError):
        original_dict = {"a": "b", "c": "b"}
        invert(original_dict)


def test_invert_basic_dictionary() -> None:
    """Example usage."""
    original_dict: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(original_dict) == {"b": "a", "d": "c"}


def test_invert_dictionary_with_longer_strings() -> None:
    """Although strings have multiple words, the strings should not invert."""
    original_dict: dict[str, str] = {"Apple Bees": "Panera Bread", "California Pizza Kitchen": "Mediterranean Deli"}
    assert invert(original_dict) == {"Panera Bread": "Apple Bees", "Mediterranean Deli": "California Pizza Kitchen"}


def test_favorite_color_all_occur_same_amount() -> None: 
    """If each color occurs the same time then the first color should return."""
    colors: dict[str, str] = {"Nupur": "blue", "Lillian": "green"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_all_have_different_frequencies() -> None: 
    """If each color occurs different times, the most popular should still return."""
    colors: dict[str, str] = {"Nupur": "blue", "Lillian": "green", "Erika": "green", "Louisa": "orange", "Jonathan": "orange", "MK": "orange"}
    assert favorite_color(colors) == "orange" 


def test_favorite_color_empty() -> None: 
    """If an empty dictionary is given, an empty string should result."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == "" 


def test_favorite_color_some_ties() -> None: 
    """If there are multiple ties but also others in the dictionary, the first that occurs the most should return."""
    colors: dict[str, str] = {"Nupur": "blue", "Lillian": "blue", "Erika": "blue", "Louisa": "orange", "Jonathan": "orange", "MK": "orange", "Meredith": "green", "Lydia": "green"}
    assert favorite_color(colors) == "blue" 


def test_invert_empty_dictionary() -> None:
    """Empty dictionary should return an empty dictionary."""
    original_dict: dict[str, str] = {}
    assert invert(original_dict) == {}


def test_count_empty_list() -> None:
    """Empty list should return an empty dictionary."""
    list0: list[str] = []
    assert count(list0) == {}


def test_count_equal_occurrences() -> None:
    """If strings occur the same amount of times the count should be the same."""   
    list0: list[str] = ["a", "a", "b", "b"]
    assert count(list0) == {"a": 2, "b": 2}


def test_count_basic_use() -> None:
    """Basic use."""
    list0: list[str] = ["a", "b", "c", "c", "d"]
    assert count(list0) == {'a': 1, 'b': 1, 'c': 2, 'd': 1} 
