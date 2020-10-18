import json
from sys import stderr

filename = 'user_info.json'


def get_user_info(filename):
    """ Get user information if available """
    try:
        with open(filename) as f:
            user_info = json.load(f)
    except:
        return None
    else:
        return user_info


user_info = get_user_info(filename)
if user_info:
    print(user_info)
