"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730391424"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
SECRET: int = int(randint(1, 4))
if SECRET == 1: 
    print("You are going to have a delicious meal today!")
else: 
    if SECRET == 2: 
        print("You'll receive amazing feedback on something you've been working on!")
    else: 
        if SECRET == 3: 
            print("The weather is going to be just how you like it today!")
        else: 
            if SECRET == 4: 
                print("You will reconnect with someone you have not spoken to in a while and it will be an amazing conversation!")
print("Now, go spread positive vibes!")