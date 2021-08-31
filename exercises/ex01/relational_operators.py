"""A program that shows how relational operators work."""
__author__ = "730391424"
a: str = input("Choose a whole number for the left-hand side of the equations. ")
b: str = input("Choose a whole number for the right-hand side of the equations. ")
c = int(a)
d = int(b)
print(a + " < " + b + " is " + str(c < d))
print(a + " >= " + b + " is " + str(c >= d))
print(a + " == " + b + " is " + str(c == d)) 
print(a + " != " + b + " is " + str(c != d))