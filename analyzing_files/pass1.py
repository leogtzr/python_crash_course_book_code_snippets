from sys import stderr


def count_words(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        stderr.write("error: '%s' does not exist\n" % filename)
        pass
    else:
        words = content.split()
        number_of_words = len(words)
        print(f"File \"{filename}\" has {number_of_words}")


files = ['in.txt', 'kaka.txt', 'names.txt']

for file in files:
    count_words(file)
