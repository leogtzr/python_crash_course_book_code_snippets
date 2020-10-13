squares = []

for n in range(1, 11):
    sq = n ** 2
    squares.append(sq)

print(squares)

squares2 = [n**2 for n in range(1, 11)]
print(squares2)

for val in (n**2 for n in range(1, 11)):
    print(val)
