filename = 'in/randoms.txt'

digit_string = ''

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    digit_string += line.strip()

# Only the first 50 numbers:
print(digit_string[:100])
