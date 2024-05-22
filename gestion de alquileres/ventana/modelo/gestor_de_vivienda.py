
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
            return "La casa ya existe."
        else:
            self.houses[name] = House(address, name, rent_price)
            return "Casa añadida correctamente."

    def remove_house(self, name):
        if name in self.houses:
            del self.houses[name]
            return "Casa eliminada correctamente."
        else:
            return "La casa no existe."

    def get_house(self, name):
        return self.houses.get(name, None)

class RentalManager:
    def __init__(self):
        self.rentals = {}

    def rent_house(self, house_name, renter, payment_date, amount):
        house = house_manager.get_house(house_name)
        if not house:
            return "La vivienda no está registrada."
        if amount != house.rent_price:
            return f"El monto del pago debe ser exactamente {house.rent_price}."
        if house_name in self.rentals:
            self.rentals[house_name].append((renter, payment_date, amount))
        else:
            self.rentals[house_name] = [(renter, payment_date, amount)]
        return "Pago de alquiler registrado exitosamente."

    def get_rentals_for_house(self, house_name):
        return self.rentals.get(house_name, [])

house_manager = HouseManager()
rental_manager = RentalManager()