"""Counting letters in a string."""

__author__ = "730391424"


# Begin your solution here...
letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
i = int = 0 
b = int = 0
while i < len(word):
    if letter == word[i]:
        b += 1
    i = i + 1
print(b)