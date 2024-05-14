class House:
    def __init__(self, address, name, rent_price):
        self.address = address
        self.name = name
        self.rent_price = rent_price

class HouseManager:
    def __init__(self):
        self.houses = {}

    def add_house(self, address, name, rent_price):
        if name in self.houses:
            return False  # La casa ya existe
        else:
            self.houses[name] = House(address, name, rent_price)
            return True  # Casa añadida correctamente

    def remove_house(self, name):
        if name in self.houses:
            del self.houses[name]
            return True  # Casa eliminada correctamente
        else:
            return False  # La casa no existe

    def get_house(self, name):
        return self.houses.get(name, None)