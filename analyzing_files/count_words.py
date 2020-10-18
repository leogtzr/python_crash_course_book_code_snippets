from sys import exit, stderr

filename = 'in.txt'

try:
    with open(filename) as file_object:
        content = file_object.read()
except FileNotFoundError:
    stderr.write(f"cannot find {filename}")

words = content.split()

number_of_words = len(words)

print(f"File \"{filename}\" has {number_of_words}")
