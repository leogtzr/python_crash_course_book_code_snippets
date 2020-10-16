def some_func(names):
    names[0] = names[0].title()

names = ['brenda', 'leo', 'edgar', 'maría', 'edgar']

some_func(names)
print(names)

names[0] = 'brendiux'
print(names)

# Passing a copy
some_func(names[:])
