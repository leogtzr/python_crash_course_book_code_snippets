responses = {}

active = True

while active:
    name = input("What's your name? ")
    response = input("Yes or no: ")

    responses[name] = response

    quit = input("Quit? ")

    if quit == 'quit':
        active = False


for name, responspe in responses.items():
    print("%s -> %s" % (name, response))
