"""Dictionary Unit Test Functions for EX03"""

__author__: str = "730486387"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len
import pytest


def test_invert_regular() -> None:
    """Use case: Test invert with multiple key-value pairs."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single() -> None:
    """Use case: Test invert with single key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_empty() -> None:
    """Edge case: Test invert function when dictionary is empty."""
    assert invert({}) == {}


def test_invert_error() -> None:
    """KeyError: Test for the invert function to see if the KeyError is raised."""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_regular() -> None:
    """Use Case: Test count with a list of repeated and unique items."""
    assert count(["nike", "adidas", "nike", "lulu", "adidas", "adidas"]) == {
        "nike": 2,
        "adidas": 3,
        "lulu": 1,
    }


def test_count_single() -> None:
    """Use Case: Test count with a list containing one repeated item."""
    assert count(["go", "go", "go"]) == {"go": 3}


def test_count_empty() -> None:
    """Edge Case: Test count with an empty list."""
    assert count([]) == {}


def test_favorite_color_regular() -> None:
    """Use Case: Test favorite color with mix of colors."""
    assert (
        favorite_color({"Ruby": "blue", "Henry": "blue", "Carly": "yellow"}) == "blue"
    )


def test_favorite_color_tie() -> None:
    """Use case: Test favorite_color when tied and return first color."""
    assert (
        favorite_color(
            {"Ruby": "blue", "Henry": "blue", "Carly": "yellow", "Victoria": "yellow"}
        )
        == "blue"
    )


def test_favorite_color_empty() -> None:
    """Egde Case: Test favorite_color when dictionary is empty."""
    assert favorite_color({}) == ""


def test_bin_len_regular() -> None:
    """Use Case: Test bin_len when list of unique words have different lengths."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_single() -> None:
    """Use Case: Test bin_len with repeated word in the list."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_empty() -> None:
    """Edge Case: Test bin_len when list is empty."""
    assert bin_len([]) == {}


def test_bin_len_vary_length() -> None:
    """Use Case: Test bin_len when word lengths vary and duplicates exist."""
    assert bin_len(["a", "aa", "b", "bb", "ccc"]) == {
        1: {"a", "b"},
        2: {"aa", "bb"},
        3: {"ccc"},
    }
