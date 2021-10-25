"""Example of functions imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None: 
    print(powerful(2, 16))
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n 


if __name__ == "__main__":
    # python idiom typically you would call main here 
    print(f"helpers.py: {__name__}")
    print("Evaluated as a program")
# else:
    # typically not common to do anything in the case where a module is imported 
    # print("Evaluated as an imported module")