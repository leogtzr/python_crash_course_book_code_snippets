names = ['leo', 'brenda', 'edgar', 'maría', 'edgar']

for x in range(1, len(names) + 1):
    print(names[-x])

# Using reversed():

print("~~~~~~~~~~~~~~~~~~~~~~~~~> ")
for name in reversed(names):
    print(name)

print("~~~~~~~~~~~~~~~~~~~~<<")

# Using individual items:
print(f"My name is: {names[0].title()}")
