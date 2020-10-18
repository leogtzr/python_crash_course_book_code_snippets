filename = 'tamal.txt'

try:
    with open(filename) as file_object:
        print(file_object.readlines())
except FileNotFoundError:
    print(f"file: {filename} does not exist")
