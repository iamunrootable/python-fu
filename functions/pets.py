def describe_pet(animal_type, pet_name):
    """Display Inforamtion About Pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet(animal_type='hamster', pet_name='billy')
describe_pet(pet_name='billy', animal_type='hamster')