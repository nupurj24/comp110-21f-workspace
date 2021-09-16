"""Finding duplicate letters in a word."""

__author__ = "730391424"

word: str = input("Enter a word: ")
dup: bool = False
i: int = 0
while i < len(word):
    char = word[i]
    j: int = i + 1
    while j < len(word): 
        if word[j] == char: 
            dup: bool = True
        j: int = j + 1 
    i: int = i + 1
print("Found duplicate: " + str(dup)) 