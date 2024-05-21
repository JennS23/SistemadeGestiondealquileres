import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, user_id, password):
        if user_id in self.users:
            return "El usuario ya existe. Por favor, elige otro ID."
        else:
            self.users[user_id] = User(user_id, password)
            return "Usuario registrado exitosamente."

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return "Usuario eliminado exitosamente."
        else:
            return "El usuario no existe."

    def login_user(self, user_id, password):
        if user_id in self.users:
            if self.users[user_id].password == password:
                return "Inicio de sesión exitoso."
            else:
                return "Contraseña incorrecta."
        else:
            return "El usuario no existe."

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

# Funciones de la interfaz
def register_user():
    user_id = entry_user_id.get()
    password = entry_password.get()
    message = user_manager.register_user(user_id, password)
    messagebox.showinfo("Registro de Usuario", message)

def delete_user():
    user_id = entry_user_id.get()
    message = user_manager.delete_user(user_id)
    messagebox.showinfo("Eliminación de Usuario", message)

def login_user():
    user_id = entry_user_id.get()
    password = entry_password.get()
    message = user_manager.login_user(user_id, password)
    if message == "Inicio de sesión exitoso.":
        root.withdraw()
        open_rental_manager()
    else:
        messagebox.showerror("Inicio de Sesión", message)

def add_house():
    address = entry_address.get()
    name = entry_house_name.get()
    rent_price = float(entry_rent_price.get())
    message = house_manager.add_house(address, name, rent_price)
    label_house_message.config(text=message)

def rent_house():
    house_name = entry_rental_house_name.get()
    renter = entry_renter.get()
    payment_date = entry_payment_date.get()
    amount = float(entry_amount.get())
    message = rental_manager.rent_house(house_name, renter, payment_date, amount)
    label_rental_message.config(text=message)

def show_rentals():
    house_name = entry_rental_house_name.get()
    rentals = rental_manager.get_rentals_for_house(house_name)
    rentals_text = "\n".join([f"{r[0]} pagó {r[2]} el {r[1]}" for r in rentals])
    label_rentals.config(text=rentals_text)
def show_houses():
    houses_text = "\n".join([f"{house.name} ({house.address})" for house in house_manager.houses.values()])
    label_house_message.config(text=houses_text)

def remove_house():
    house_name = entry_house_name.get()
    message = house_manager.remove_house(house_name)
    label_house_message.config(text=message)
def open_rental_manager():
    rental_window = tk.Toplevel(root)
    rental_window.title("Gestor de Alquileres")
    rental_window.geometry("600x600")  # Ancho x Alto

    # Marco para registrar casas
    frame_house = tk.Frame(rental_window)
    frame_house.pack(pady=20)

    global entry_address, entry_house_name, entry_rent_price, label_house_message
    label_address = tk.Label(frame_house, text="Dirección de la Casa:")
    label_address.pack(pady=5)
    entry_address = tk.Entry(frame_house, width=30)
    entry_address.pack(pady=5)

    label_house_name = tk.Label(frame_house, text="Nombre de la Casa:")
    label_house_name.pack(pady=5)
    entry_house_name = tk.Entry(frame_house, width=30)
    entry_house_name.pack(pady=5)

    label_rent_price = tk.Label(frame_house, text="Precio del Alquiler:")
    label_rent_price.pack(pady=5)
    entry_rent_price = tk.Entry(frame_house, width=30)
    entry_rent_price.pack(pady=5)

    add_house_button = tk.Button(frame_house, text="Añadir Casa", command=add_house)
    add_house_button.pack(pady=5)

    show_houses_button = tk.Button(frame_house, text="Mostrar Casas", command=show_houses)
    show_houses_button.pack(pady=5)

    remove_house_button = tk.Button(frame_house, text="Eliminar Casa", command=remove_house)
    remove_house_button.pack(pady=5)

    label_house_message = tk.Label(frame_house, text="")
    label_house_message.pack(pady=10)

    # Marco para registrar pagos de alquiler
    frame_rental = tk.Frame(rental_window)
    frame_rental.pack(pady=20)

    global entry_rental_house_name, entry_renter, entry_payment_date, entry_amount, label_rental_message, label_rentals
    label_rental_house_name = tk.Label(frame_rental, text="Nombre de la Casa:")
    label_rental_house_name.pack(pady=5)
    entry_rental_house_name = tk.Entry(frame_rental, width=30)
    entry_rental_house_name.pack(pady=5)

    label_renter = tk.Label(frame_rental, text="Nombre del Inquilino:")
    label_renter.pack(pady=5)
    entry_renter = tk.Entry(frame_rental, width=30)
    entry_renter.pack(pady=5)

    label_payment_date = tk.Label(frame_rental, text="Fecha de Pago:")
    label_payment_date.pack(pady=5)
    entry_payment_date = tk.Entry(frame_rental, width=30)
    entry_payment_date.pack(pady=5)

    label_amount = tk.Label(frame_rental, text="Monto del Pago:")
    label_amount.pack(pady=5)
    entry_amount = tk.Entry(frame_rental, width=30)
    entry_amount.pack(pady=5)

    rent_house_button = tk.Button(frame_rental, text="Registrar Pago", command=rent_house)
    rent_house_button.pack(pady=5)

    show_rentals_button = tk.Button(frame_rental, text="Mostrar Pagos", command=show_rentals)
    show_rentals_button.pack(pady=5)

    label_rental_message = tk.Label(frame_rental, text="")
    label_rental_message.pack(pady=10)

    label_rentals = tk.Label(frame_rental, text="", justify="left")
    label_rentals.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Usuarios")
root.geometry("400x350")  # Ancho x Alto

# Crear un marco para los widgets
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Crear los Entry widgets y etiquetas para la gestión de usuarios
label_user_id = tk.Label(frame, text="ID de Usuario:")
label_user_id.pack(pady=5)
entry_user_id = tk.Entry(frame, width=30)
entry_user_id.pack(pady=5)

label_password = tk.Label(frame, text="Contraseña:")
label_password.pack(pady=5)
entry_password = tk.Entry(frame, width=30, show='*')
entry_password.pack(pady=5)

# Crear los botones para la gestión de usuarios
register_button = tk.Button(frame, text="Registrar", command=register_user)
register_button.pack(pady=5)

delete_button = tk.Button(frame, text="Eliminar", command=delete_user)
delete_button.pack(pady=5)

login_button = tk.Button(frame, text="Iniciar Sesión", command=login_user)
login_button.pack(pady=5)

# Crear instancias de UserManager, HouseManager y RentalManager
user_manager = UserManager()
house_manager = HouseManager()
rental_manager = RentalManager()

# Iniciar el bucle principal de la interfaz
root.mainloop()
