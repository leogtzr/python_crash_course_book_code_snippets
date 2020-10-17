def print_names(*names):
    for name in names:
        print(name)

    print("!~!!!~!!")

    print(f"First element of the tuple is: {names[0].title()}")

#print_names(['Leo', 'Brenda'])
#print_names(['Leo', 'Brenda'])


print_names("leo", "brenda")

# Note: Variadic arguments are handled as tuples.
# Note 2: As in other languages, variadic arguments need to be positionated at the end of the list of parameters
# to avoid confusion.
# You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this.
