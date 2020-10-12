def print_elements(names):
    print("~~~~~~~~~~~~~~~~~~~~~~~~ /BEGIN>")
    for name in names:
        print(name)
    print("~~~~~~~~~~~~~~~~~~~~~~~~ /END>")


motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[0]

print_elements(motorcycles)

# Removing the last element:
del motorcycles[-1]

print_elements(motorcycles)

vals = []
for n in range(1, 5):
    vals.append(n)

while len(vals) > 0:
    print(vals[-1])
    del vals[-1]
