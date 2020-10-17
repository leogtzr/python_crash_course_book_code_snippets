# This is some kind of try-with-resources
with open('in/pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents.rstrip())
