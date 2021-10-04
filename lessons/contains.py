"""Example of a function that processes a list."""

# define a function named contains 
# we can give ttwo arguments: a needle value we're searching for in a haystack list\


def main() -> None: 
    names: list[str] = ["Kris", "Kaki", "Kris"]
    print(contains("Kris", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True of needle is found in haystack, False otherwise."""
    i: int = 0
    while i < len(haystack): 
        if haystack[i] == needle:
            return True
        i += 1
    return False


if __name__ == "__main__":
    main()

    # return true if needle is found in haystack, false otherwise 
    # loop through each index in list 
    # test if item stored at index is equal to needle
# return true if so 
# returm false afrer testing each line 