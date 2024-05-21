import tkinter as tk

from modelo.gestor_de_usuarios import *


def login_user():
    user_id = entry_user_id.get()
    password = entry_password.get()
    message = user_manager.login_user(user_id, password)
    label_message.config(text=message)

def register_user():
    user_id = entry_user_id.get()
    password = entry_password.get()
    message = user_manager.register_user(user_id, password)
    label_message.config(text=message)


def delete_user():
    user_id = entry_user_id.get()
    message = user_manager.delete_user(user_id)
    label_message.config(text=message)


#Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Usuarios")
root.geometry("400x350")  # Ancho x Alto

#Crear un marco para los widgets
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#Crear los Entry widgets y etiquetas
label_user_id = tk.Label(frame, text="ID de Usuario:")
label_user_id.pack(pady=5)
entry_user_id = tk.Entry(frame, width=30)
entry_user_id.pack(pady=5)

label_password = tk.Label(frame, text="Contraseña:")
label_password.pack(pady=5)
entry_password = tk.Entry(frame, width=30, show='*')
entry_password.pack(pady=5)

#Crear los botones

login_button = tk.Button(frame, text="Iniciar Sesión", command=login_user)
login_button.pack(pady=5)

register_button = tk.Button(frame, text="Registrar", command=register_user)
register_button.pack(pady=5)

delete_button = tk.Button(frame, text="Eliminar", command=delete_user)
delete_button.pack(pady=5)


#Crear una etiqueta para mostrar mensajes
label_message = tk.Label(frame, text="")
label_message.pack(pady=10)

#Crear una instancia de UserManager
user_manager = UserManager()

root.mainloop()