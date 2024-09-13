# lib/owner.py
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to the pet if it is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a sorted list of pets by their name."""
        return sorted(self.pets(), key=lambda pet: pet.name)


# lib/pet.py
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
