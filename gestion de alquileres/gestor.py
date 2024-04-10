import datetime

class Usuario:
    def __init__(self, nombre, correo, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña

class Propiedad:
    def __init__(self, direccion, descripcion, num_habitaciones, superficie):
        self.direccion = direccion
        self.descripcion = descripcion
        self.num_habitaciones = num_habitaciones
        self.superficie = superficie

class ContratoAlquiler:
    def _init_(self, arrendatario, propiedad, fecha_inicio, fecha_fin, renta_mensual, fianza):
        self.arrendatario = arrendatario
        self.propiedad = propiedad
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.renta_mensual = renta_mensual
        self.fianza = fianza

    def _str_(self):
        return f"Contrato de alquiler de {self.propiedad} para {self.arrendatario}"

class GestorContratos:
    def _init_(self):
        self.contratos = []

    def crear_contrato(self, arrendatario, propiedad, fecha_inicio, fecha_fin, renta_mensual, fianza):
        nuevo_contrato = ContratoAlquiler(arrendatario, propiedad, fecha_inicio, fecha_fin, renta_mensual, fianza)
        self.contratos.append(nuevo_contrato)
        print("Contrato creado exitosamente.")

    def modificar_contrato(self, indice, nuevo_arrendatario):
        if 0 <= indice < len(self.contratos):
            self.contratos[indice].arrendatario = nuevo_arrendatario
            print("Contrato modificado exitosamente.")
        else:
            print("Índice de contrato inválido.")

    def eliminar_contrato(self, indice):
        if 0 <= indice < len(self.contratos):
            del self.contratos[indice]
            print("Contrato eliminado exitosamente.")
        else:
            print("Índice de contrato inválido.")

class PagoRenta:
    def __init__(self, fecha_pago, importe):
        self.fecha_pago = fecha_pago
        self.importe = importe

class Incidencia:
    def __init__(self, descripcion, fecha, estado):
        self.descripcion = descripcion
        self.fecha = fecha
        self.estado = estado


def registrar_usuario(usuarios):
    print("\nRegistro de Nuevo Usuario:")
    nombre = input("Ingrese el nombre del nuevo usuario: ")
    correo = input("Ingrese el correo electrónico del nuevo usuario: ")
    contraseña = input("Ingrese la contraseña del nuevo usuario: ")
    nuevo_usuario = Usuario(nombre, correo, contraseña)
    usuarios.append(nuevo_usuario)
    print("Usuario registrado correctamente.")

def borrar_usuario(usuarios):
    print("\nBorrar Usuario:")
    nombre = input("Ingrese el nombre del usuario que desea borrar: ")
    for usuario in usuarios:
        if usuario.nombre == nombre:
            usuarios.remove(usuario)
            print(f"Usuario {nombre} borrado correctamente.")
            return
    print(f"No se encontró ningún usuario con el nombre {nombre}.")

def modificar_informacion_usuario(usuarios):
    print("\nModificar Información de Usuario:")
    nombre = input("Ingrese el nombre del usuario que desea modificar: ")
    for usuario in usuarios:
        if usuario.nombre == nombre:
            print("Ingrese los nuevos datos del usuario:")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_correo = input("Nuevo correo electrónico: ")
            nueva_contraseña = input("Nueva contraseña: ")
            usuario.nombre = nuevo_nombre
            usuario.correo = nuevo_correo
            usuario.contraseña = nueva_contraseña
            print(f"Información de usuario {nombre} modificada correctamente.")
            return
    print(f"No se encontró ningún usuario con el nombre {nombre}.")


def mostrar_menu():
    print("\nMenú de Usuario:")
    print("1. Registrar nuevo usuario")
    print("2. Borrar usuario existente")
    print("3. Modificar información de usuario")
    print("4. Crear contrato de alquiler")
    print("5. Modificar contrato de alquiler")
    print("6. Eliminar contrato de alquiler")
    print("7. Ver información del contrato de alquiler")
    print("8. Realizar pago de renta")
    print("9. Notificar incidencia")
    print("10. Salir")

def main():
    usuarios = []
    propiedades = []
    gestor_contratos = GestorContratos()

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            borrar_usuario(usuarios)
        elif opcion == "3":
            modificar_informacion_usuario(usuarios)
        elif opcion == "4":
            crear_contrato_alquiler(usuarios, propiedades, gestor_contratos)
        elif opcion == "5":
            modificar_contrato_alquiler(gestor_contratos)
        elif opcion == "6":
            eliminar_contrato_alquiler(gestor_contratos)
        elif opcion == "7":
            ver_informacion_contrato(gestor_contratos)
        elif opcion == "8":
            # Realizar pago de renta
            fecha_pago = datetime.datetime.now()
            importe = float(input("Ingrese el importe del pago de renta: "))
            pago_renta = PagoRenta(fecha_pago, importe)
            print("Pago de renta realizado exitosamente.")
        elif opcion == "9":
            # Notificar incidencia
            descripcion = input("Describa la incidencia: ")
            fecha_incidencia = datetime.datetime.now()
            incidencia = Incidencia(descripcion, fecha_incidencia, "Pendiente")
            print("Incidencia notificada correctamente.")
        elif opcion == "10":
            # Salir del programa
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 10.")

if __name__ == "__main__":
    main()
