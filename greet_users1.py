def greet_users(names):
    """ Prints a simple greeting to each user in the list. """
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


greet_users(['Brenda', 'Leo', 'Edgar', 'María', 'Edgar'])
