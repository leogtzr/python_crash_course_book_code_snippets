def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='cat', pet_name='Ramona')
# Now having these variable names when calling the function I can vary the order.
describe_pet(pet_name='Ramona', animal_type='cat')
