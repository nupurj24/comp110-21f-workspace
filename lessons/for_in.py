"""An example of for in syntax."""

names: list[str] = ["Nupur", "Jess", "Harliv", "Tony"]

# example of iterating throughh names using a while loop
print("while output:")
i: int = 0 
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for...in output")
# the following for...in loop is the same as the while loop above
for name in names:
    print(name)
 