def build_person(first_name, last_name):
    """ Returns a dictionary """
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('Leo', 'Gtz')

print(musician)
