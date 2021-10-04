"""Repeating a beat in a loop."""

__author__ = "730391424"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
# Consider having a str variable, separate from the beat, that you can add to in a repetitive fashion.
space: str = " "
if repeat <= 0:
    print("No beat...")
a: str = ""
while repeat > 0:
    if repeat == 1:
        a += beat
    else: 
        a += beat + space
    repeat = repeat - 1
print(a)                                       