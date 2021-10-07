"""List utility functions part 2."""

__author__ = "730391424"

# Define your functions below


def main() -> None: 
    """Main."""
    input_list: list[int] = [2, 3, 4, 5]
    print(only_evens(input_list))
    a_list: list[int] = [1, 3, 5, 6]
    start: int = 1
    end: int = 7
    print(sub(a_list, start, end))
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    print(concat(list_1, list_2))


def only_evens(input_list: list[int]) -> list[int]:
    """A function that returns only the even numbers in a list."""
    i: int = 0
    evens_list: list[int] = []
    while i < len(input_list):
        if input_list[i] % 2 == 0:
            evens_list.append(input_list[i])
        i += 1
    return evens_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """A function that gives a subset of a list."""
    new_list: list[int] = []
    if start > len(a_list):
        return new_list
    if len(a_list) == 0:
        return new_list
    if end <= 0:
        return new_list
    if start < 0:
        start = 0
    i: int = start 
    while i < end:
        new_list.append(a_list[i])
        i += 1
    if end > len(a_list):
        end = len(a_list) - 1
        while i <= end:
            new_list.append(a_list[i])
            i += 1
    else:
        while i < end:
            new_list.append(a_list[i])
            i += 1
    return new_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """A function that concatenates two lists."""
    concat_list: list[int] = list_1
    i: int = 0 
    while i < len(list_2):
        concat_list.append(list_2[i])
        i += 1
    return concat_list


if __name__ == "__main__":
    main()