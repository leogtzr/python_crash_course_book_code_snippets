def build_person(first_name, last_name, age=None):
    """ Returns a dictionary """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Leo', 'Gtz')

print(musician)

father = build_person('Edgar', 'Gutierrez', 49)
print(father)
