def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

def myf(name='Leo'):
    print(f"Hello, {name.title()}")

describe_pet(pet_name='Willie')
myf('Leonardo')
myf()




# NOTE

# When you use default values, any parameter with a default value needs to be listed after all the 
# parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly.

