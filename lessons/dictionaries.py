"""Demonstrations of dictionary capabilities."""

# declaring the type of a dictionary 
schools: dict[str, int]

# Initialize an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Acess a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary by its key.
# schools.pop("Duke")

# Test for the existence of a key 
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present: {is_duke_present}")

# update or reassign a key-value pair 
schools["UNC"] = 20000
schools["NCSU"] += 200

# Print a dictionary literal representation 
print(schools)

# Demonstration of dictionary literals 

# Empty dictionary literal 
schools = {}  # same as dict()
print(schools)

# alternatively, initialize key-value pairs 
schools = {
    "UNC": 19400, 
    "Dukie": 6717, 
    "NCSU": 26150}
# you can put them on separate lines or same lines, its based on whats easy to read 
print(schools)

# What happens when a key does not exist 
# print(schools["UNCC"])
# Example looping over the keys of a dict 
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")