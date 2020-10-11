def print_elements(names):
    print("~~~~~~~~~~~~~~~~~~~~~~~~ /BEGIN>")
    for name in names:
        print(name)
    print("~~~~~~~~~~~~~~~~~~~~~~~~ /END>")


names = ['brenda', 'edgar', 'maría', 'edgar']
names.append('leo')

print_elements(names)

last_element = names.pop()

print_elements(names)
print(last_element)

names.insert(1, 'other')

print_elements(names)

# You can add a new element at any position in your list by using the insert() method.
# You do this by specifying the index of the new element and the value of the new item.
names.insert(len(names), last_element)

print_elements(names)
