from main import *
import tkinter as tk
from tkinter import messagebox
import datetime
import uuid

# Aquí irían las clases y funciones definidas previamente

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestión de Alquileres")
        self.sistema_alquileres = SistemaGestionAlquileres()

        self.label_nombre_usuario = tk.Label(master, text="Nombre de Usuario:")
        self.label_nombre_usuario.grid(row=0, column=0)
        self.entry_nombre_usuario = tk.Entry(master)
        self.entry_nombre_usuario.grid(row=0, column=1)

        self.label_direccion_propiedad = tk.Label(master, text="Dirección de Propiedad:")
        self.label_direccion_propiedad.grid(row=1, column=0)
        self.entry_direccion_propiedad = tk.Entry(master)
        self.entry_direccion_propiedad.grid(row=1, column=1)

        self.label_fecha_inicio = tk.Label(master, text="Fecha de Inicio:")
        self.label_fecha_inicio.grid(row=2, column=0)
        self.entry_fecha_inicio = tk.Entry(master)
        self.entry_fecha_inicio.grid(row=2, column=1)

        self.label_fecha_fin = tk.Label(master, text="Fecha de Fin:")
        self.label_fecha_fin.grid(row=3, column=0)
        self.entry_fecha_fin = tk.Entry(master)
        self.entry_fecha_fin.grid(row=3, column=1)

        self.button_registrar_usuario = tk.Button(master, text="Registrar Usuario", command=self.registrar_usuario)
        self.button_registrar_usuario.grid(row=4, column=0)

        self.button_registrar_propiedad = tk.Button(master, text="Registrar Propiedad", command=self.registrar_propiedad)
        self.button_registrar_propiedad.grid(row=4, column=1)

        self.button_crear_contrato = tk.Button(master, text="Crear Contrato", command=self.crear_contrato)
        self.button_crear_contrato.grid(row=5, column=0)

    def registrar_usuario(self):
        nombre_usuario = self.entry_nombre_usuario.get()
        if nombre_usuario:
            self.sistema_alquileres.registrar_usuario(nombre_usuario)
            messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente")
            self.entry_nombre_usuario.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor ingrese un nombre de usuario")

    def registrar_propiedad(self):
        def registrar_propiedad(self):
            direccion_propiedad = self.entry_direccion_propiedad.get()
            descripcion = "Descripción temporal"  # Aquí debes obtener la descripción de alguna manera
            numero_habitaciones = 0  # Aquí debes obtener el número de habitaciones de alguna manera
            superficie = 0.0  # Aquí debes obtener la superficie de alguna manera
            arrendador = "Arrendador temporal"  # Aquí debes obtener el arrendador de alguna manera
            if direccion_propiedad:
                self.sistema_alquileres.registrar_propiedad(direccion_propiedad, descripcion, numero_habitaciones,
                                                            superficie, arrendador)
                messagebox.showinfo("Registro Exitoso", "Propiedad registrada exitosamente")
                self.entry_direccion_propiedad.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Por favor ingrese una dirección de propiedad")


    def crear_contrato(self):
        nombre_usuario = self.entry_nombre_usuario.get()
        direccion_propiedad = self.entry_direccion_propiedad.get()
        fecha_inicio = self.entry_fecha_inicio.get()
        fecha_fin = self.entry_fecha_fin.get()
        if nombre_usuario and direccion_propiedad and fecha_inicio and fecha_fin:
            usuario = next((u for u in self.sistema_alquileres.usuarios if u.nombre == nombre_usuario), None)
            propiedad = next((p for p in self.sistema_alquileres.propiedades if p.direccion == direccion_propiedad), None)
            if usuario and propiedad:
                fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y")
                fecha_fin = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y")
                self.sistema_alquileres.crear_contrato_alquiler(usuario, propiedad, fecha_inicio, fecha_fin)
                messagebox.showinfo("Contrato Creado", "Contrato de alquiler creado exitosamente")
                self.entry_nombre_usuario.delete(0, tk.END)
                self.entry_direccion_propiedad.delete(0, tk.END)
                self.entry_fecha_inicio.delete(0, tk.END)
                self.entry_fecha_fin.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Usuario o propiedad no encontrados")
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos")

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
