names = ['leo', 'brenda', 'edgar', 'maría', 'edgar']
for name in names:
    print(name)

# First element:
print("First element is: %s" % names[0])

# Last element:
print(names[len(names) - 1])

# Negative indexing:
print("Last: %s" % names[-1])

# Penultimate position
print("-> %s" % names[-2])

# Assignment:
names[0] = names[0].title()
print("First: %s" % names[0])

names[0] = names[0].upper()
print("First: %s" % names[0])

# Deletion:
del names[0]
print(names[0])             # now "brenda" is the first element.
