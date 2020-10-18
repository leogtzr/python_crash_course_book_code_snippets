from sys import exit, stderr


def count_words(filename):
    try:
        with open(filename) as file_object:
            content = file_object.read()

    except FileNotFoundError:
        stderr.write(f"cannot find {filename}")

    words = content.split()

    number_of_words = len(words)

    print(f"File \"{filename}\" has {number_of_words}")


filename = 'in.txt'
count_words(filename)
