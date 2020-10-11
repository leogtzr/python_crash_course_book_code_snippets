first_name = "ada"
last_name = "lovelace"

full_name = f"A[{first_name.title()}] B[{last_name.upper()}]"
print(full_name)

# F-strings were first introduced in Python 3.6.
# If you’re using Python 3.5 or earlier, you’ll need to use the format()
# method rather than this f syntax. To use format(),
# list the variables you want to use in the string inside the parentheses following format.
# Each variable is referred to by a set of braces;
# the braces will be filled by the values listed in parentheses in the order provided:

# full_name = "{} {}".format(first_name, last_name)
