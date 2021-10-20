"""Practice with dictionaries."""

__author__ = "730391424"

# Define your functions below


def main() -> None:
    """Main."""
    original_dict: dict[str, str]
    original_dict = {"a": "b", "c": "d"}
    print(invert(original_dict))
    colors: dict[str, str]
    colors = {"Nupur": "blue", "Lydia": "orange", "Ellie": "blue", "Saurya": "blue", "Meredith": "green"}
    print(favorite_color(colors))
    list0: list[str] = ["a", "b", "c", "c", "d"]
    print(count(list0))


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """A function that inverts a dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in original_dict:
        inverted_dict[original_dict[key]] = key
        if original_dict[key] in original_dict:
            raise KeyError("You can't have duplicate keys!")
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """A function that returns the most popular favorite color."""
    favorite_color: str = ""
    colors_dict: dict[str, int] = {}
    for key in colors:
        colors_dict[colors[key]] = 1
    for key in colors: 
        if colors[key] in colors_dict:
            colors_dict[colors[key]] += 1
    max: int = 1 
    for key in colors_dict:
        if colors_dict[key] > max:
            max = colors_dict[key]
            favorite_color = key
    return favorite_color


def count(list0: list[str]) -> dict[str, int]:
    """A function that keeps score."""
    count_dict: dict[str, int] = {}
    for item in list0:
        count_dict[item] = 0
    for item in list0:
        if item in count_dict: 
            count_dict[item] = count_dict[item] + 1
    return count_dict


if __name__ == "__main__":
    main()