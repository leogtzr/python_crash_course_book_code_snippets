from sys import exit

names = {'Leo', 'Brenda', 'Brenda', 'Edgar', 'María', 'Edgar'}
print(len(names))
print(names)
if len(names) != 4:
    raise Exception('Alv')


for s in [{'a', 'b', 'c'}]:
    for e in s:
        print(s)
