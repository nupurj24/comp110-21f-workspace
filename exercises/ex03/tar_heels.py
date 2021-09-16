"""An exercise in remainders and boolean logic."""

__author__ = "730391424"

# When evenly divisible by 2, print “TAR”.
# When evenly divisible by 7, print “HEELS”.
# When evenly divisible by both 2 and 7, print “TAR HEELS” instead of just “TAR” or “HEELS”
# When none of the above conditions are met, print “CAROLINA”

# Begin your solution here...
number: int = int(input("Enter an int: ")) 
a: int = number % 2
b: int = number % 7
if a == 0:
    if b == 0:
        print("TAR HEELS")
    else: 
        if a == 0: 
            print("TAR")
else:
    if b == 0: 
        print("HEELS")
    else:
        print("CAROLINA")