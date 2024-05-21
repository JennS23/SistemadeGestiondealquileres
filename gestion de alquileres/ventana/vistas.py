from tkinter import *
from modelo.gestor_de_usuarios import User, UserManager

root = Tk()

def create_centered_entry(parent, width, show):
    entry = Entry(parent, width=width, show=show)
    entry.pack(pady=10)  # Añade un poco de espacio vertical entre los Entry widgets
    return entry

#Crear la ventana principal
root.title("Gestor de Usuarios")
root.geometry("400x200")  # Ancho x Alto

#Crear un marco para centrar los Entry widgets
frame = Frame(root)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#Crear los Entry widgets centrados
entry1 = create_centered_entry(frame, width=30,show="")
entry2 = create_centered_entry(frame, width=30, show="*")

def click_boton():
    texto = Label(root, text=f'almacenado el contenido correctamente').grid(row=0, column=0)

boton1 = Button(root, text="no presiones el boton", padx=10, pady=10, command=click_boton).grid(row=0, column=0)


root.mainloop()