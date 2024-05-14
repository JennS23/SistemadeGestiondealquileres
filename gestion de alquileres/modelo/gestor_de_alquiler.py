from gestor_de_vivienda import HouseManager

class RentalManager:
    def __init__(self):
        self.rentals = {}

    def rent_house(self, house_name, renter, payment_date, amount):
        try:
            house = HouseManager().get_house(house_name)
            if not house:
                raise ValueError("La vivienda no está registrada.")
            else:
                if house_name in self.rentals:
                    self.rentals[house_name].append((renter, payment_date, amount))
                else:
                    self.rentals[house_name] = [(renter, payment_date, amount)]
                return "Pago de alquiler registrado exitosamente."
        except ValueError as e:
            return str(e)

    def get_rentals_for_house(self, house_name):
        return self.rentals.get(house_name, [])