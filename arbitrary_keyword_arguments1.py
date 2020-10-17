# The double asterisks before the parameter **user_info cause Python to create an
# empty dictionary called user_info and pack whatever name-value pairs it receives
# into this dictionary. Within the function, you can access the key-value pairs in
# user_info just as you would for any dictionary.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# You’ll often see the parameter name **kwargs used to collect non-specific keyword arguments.
