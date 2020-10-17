# This is some kind of try-with-resources
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)
