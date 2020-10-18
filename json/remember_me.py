import json

username = input("What is your name: ")

filename = 'username.json'

user_info = {}
user_info['username'] = username
user_info['age'] = 29

with open(filename, 'w') as f:
    json.dump(user_info, f)
    print(f"We'll remember you when you come back, {username}!")
