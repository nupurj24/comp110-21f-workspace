"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 1
while depth > 0:
    print(TREE * i)
    depth = depth - 1
    i = i + 1