"""List utility functions."""

__author__ = "730391424"


# TODO: Implement your functions here.


def main() -> None:
    """Main."""
    numbers: list[int] = [1, 1, 1, 1]
    match: int = 1
    print(all(numbers, match))
    list_1: list[int] = [2, 2, 2]
    list_2: list[int] = [2, 1, 2]
    print(is_equal(list_1, list_2))
    input: list[int] = [8, 7, 6]
    print(max(input))


def all(numbers: list[int], match: int) -> bool: 
    """Are all of the numbers in the list the same as the match?"""
    i: int = 0
    if len(numbers) == 0: 
        return False 
    while i <= len(numbers) - 1: 
        if numbers[i] != match:
            return False
        i += 1
    return True


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Is every element at every index equal in both lists?"""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Which number is the maximum?"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List") 
    i: int = 0
    max: int = 0
    while i < len(input):
        if input[i] > max:
            max = input[i]
        i += 1
    return max 


# if the index number is bigger than max store it as max 


if __name__ == "__main__":
    main()