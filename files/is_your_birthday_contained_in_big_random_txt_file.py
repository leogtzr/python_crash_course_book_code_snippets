filename = 'in/randoms.txt'

digit_string = ''

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    digit_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in digit_string:
    print("Your birthday appears in the file")
else:
    print("Your birthday does not appear in the file with random numbers")
