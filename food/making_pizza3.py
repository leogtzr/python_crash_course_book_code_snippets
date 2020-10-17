from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# you simply write import followed by the name of the module, makes every function
# from the module available in your program. If you use this kind of import statement
# to import an entire module named module_name.py, each function in the module is
# available through the following syntax:

#       module_name.function_name()
