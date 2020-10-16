def print_pets(pets):
    for pet in pets:
        print(pet)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

while 'cat' in pets:
    pets.remove('cat')

print_pets(pets)
