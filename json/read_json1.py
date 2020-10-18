import json

filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)
print(len(numbers))

# Doing something with the numbers gotten from the file:
print([n for n in numbers if n > 3])
