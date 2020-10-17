filename = 'in/pi_digits.txt'

lines = []

# This is some kind of try-with-resources
with open(filename) as file_object:
    for line in file_object:
        lines.append(line)

for line in lines:
    print(line.rstrip())
