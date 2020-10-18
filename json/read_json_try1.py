import json
from sys import stderr

filename = 'user_info.json'

try:
    with open(filename) as f:
        user_info = json.load(f)
except FileNotFoundError:
    stderr.write(f"File: '{filename}' does not exist.")
else:
    print("Welcome back!, %s" % user_info['username'])
    print(user_info)
