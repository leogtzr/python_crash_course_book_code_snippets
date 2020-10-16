msg = ''

until = True

while until: 
    msg = input('quit? ')

    if msg != 'quit':
        print(f"echo: {msg}")
    else:
        until = False
