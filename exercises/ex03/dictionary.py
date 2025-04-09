"""Dictionary Function"""

__author__: str = "730486387"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of dictionary."""
    """Raise KeyError if duplicate values found."""
    inverted_dict: dict[str, str] = {}
    for key in input_dict:
        value: str = input_dict[key]
        if value in inverted_dict:
            raise KeyError("Duplicate key found when inverting!")
        inverted_dict[value] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    """Each key is a unique value in the given list..."""
    """...and each value associated is the count of the number of times..."""
    """...that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(name_color_dict: dict[str, str]) -> str:
    """Return color that appears most frequently in the dictionary."""
    color_counts: dict[str, int] = {}
    for name in name_color_dict:
        color = name_color_dict[name]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    max_count = -1
    most_frequent_color = ""
    for color in color_counts:
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            most_frequent_color = color
    return most_frequent_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bin words by their length into a dictionary of lists."""
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
