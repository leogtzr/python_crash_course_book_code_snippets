names = ['Leo', 'Brenda', 'Edgar', 'Maria', 'Edgar']

names2 = names

print(names[0])
print(names2[0])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

names[0] = names[0].upper()

print(names[0])
print(names2[0])


print("sepppppp")

# To copy a list, this is a form:
names3 = names[:]
print(names[0])
print(names2[0])
print(names3[0])

names[0] = "Leonidas"

print("____________________________")
print(names[0])
print(names2[0])
print(names3[0])
