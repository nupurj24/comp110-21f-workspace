"""A program showing how numeric operators work."""
__author__ = "730391424"
a: str = input("Choose a whole number from 1-9 for the left-hand side of the equations. ")
b: str = input("Choose a whole number from 1-9 for the right-hand side of the equations. ")
c = int(a)
d = int(b)
print("Left-hand side: " + a)
print("Right-hand side: " + b)
print(a + " ** " + b + " is " + str(c ** d))  
print(a + " / " + b + " is " + str(c / d))
print(a + " // " + b + " is " + str(c // d))
print(a + " % " + b + " is " + str(c % d)) 