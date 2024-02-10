class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Nope. Needs to be an approved type. Bosse's Orders")
        self.owner = owner
        self.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        pets_to_return = []
        for pet in Pet.all:
            if pet.owner == self:
                pets_to_return.append(pet)
            else:
                pass
        return pets_to_return

    def add_pet(self, pet_object):
        if isinstance(pet_object, Pet):
            pet_object.owner = self
        else:
            raise Exception("Thats not an instance >:(")
        
    def keyGrabber(obj):
        return obj.name

    def get_sorted_pets(self):
        owners_pets = Owner.pets(self)
        sorted_pets = sorted(owners_pets, key = lambda x : x.name)
        return sorted_pets
