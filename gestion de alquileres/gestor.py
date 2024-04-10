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
    def __init__(self):
        self.contratos = []

    def crear_contrato(self, contrato):
        self.contratos.append(contrato)
        print("Contrato creado exitosamente.")

    def modificar_contrato(self, indice, nuevo_contrato):
        if 0 <= indice < len(self.contratos):
            self.contratos[indice] = nuevo_contrato
            print("Contrato modificado exitosamente.")
        else:
            print("Índice de contrato inválido.")

    def eliminar_contrato(self, indice):
        if 0 <= indice < len(self.contratos):
            del self.contratos[indice]
            print("Contrato eliminado exitosamente.")
        else:
            print("Índice de contrato inválido.")

    def mostrar_contratos(self):
        if self.contratos:
            print("Lista de contratos:")
            for i, contrato in enumerate(self.contratos):
                print(f"{i + 1}. {contrato}")
        else:
            print("No hay contratos registrados.")


class PagoRenta:
    def __init__(self, fecha_pago, importe):
        self.fecha_pago = fecha_pago
        self.importe = importe

class Incidencia:
    def __init__(self, descripcion, fecha, estado):
        self.descripcion = descripcion
        self.fecha = fecha
        self.estado = estado

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, estado="Pendiente"):
        self.tareas.append({"descripcion": descripcion, "estado": estado})

    def marcar_como_realizada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["estado"] = "Realizada"
            print("Tarea marcada como realizada.")
        else:
            print("Índice de tarea inválido.")

    def mostrar_tareas(self):
        if self.tareas:
            print("Lista de tareas:")
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea['descripcion']} - Estado: {tarea['estado']}")
        else:
            print("No hay tareas en la lista.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            print("Tarea eliminada correctamente.")
        else:
            print("Índice de tarea inválido.")

class Documento:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido

class GestionDocumentos:
    def __init__(self):
        self.documentos = []

    def almacenar_documento(self, nombre, contenido):
        nuevo_documento = Documento(nombre, contenido)
        self.documentos.append(nuevo_documento)
        print("Documento almacenado correctamente.")

    def descargar_documento(self, nombre_documento):
        for documento in self.documentos:
            if documento.nombre == nombre_documento:
                return documento.contenido
        return None


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

def menu_gestor_contratos(gestor_contratos):
    while True:
        print("\nMenú de Gestor de Contratos:")
        print("1. Crear contrato")
        print("2. Modificar contrato")
        print("3. Eliminar contrato")
        print("4. Mostrar lista de contratos")
        print("5. Volver al menú principal")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            arrendatario = input("Ingrese el nombre del arrendatario: ")
            propiedad = input("Ingrese la dirección de la propiedad: ")
            fecha_inicio = input("Ingrese la fecha de inicio del contrato (YYYY-MM-DD): ")
            fecha_fin = input("Ingrese la fecha de fin del contrato (YYYY-MM-DD): ")
            renta_mensual = float(input("Ingrese la renta mensual: "))
            fianza = float(input("Ingrese el monto de la fianza: "))

            # Crear una instancia de ContratoAlquiler con la información proporcionada
            nuevo_contrato = ContratoAlquiler(arrendatario, propiedad, fecha_inicio, fecha_fin, renta_mensual, fianza)

            gestor_contratos.crear_contrato(nuevo_contrato)
        elif opcion == "2":
            gestor_contratos.mostrar_contratos()
            indice_contrato = int(input("Ingrese el índice del contrato que desea modificar: ")) - 1
            if 0 <= indice_contrato < len(gestor_contratos.contratos):
                nuevo_arrendatario = input("Ingrese el nuevo arrendatario: ")
                nuevo_propiedad = input("Ingrese la nueva dirección de la propiedad: ")
                nueva_fecha_inicio = input("Ingrese la nueva fecha de inicio del contrato (YYYY-MM-DD): ")
                nueva_fecha_fin = input("Ingrese la nueva fecha de fin del contrato (YYYY-MM-DD): ")
                nueva_renta_mensual = float(input("Ingrese la nueva renta mensual: "))
                nueva_fianza = float(input("Ingrese el nuevo monto de la fianza: "))

                # Crear una instancia de ContratoAlquiler con la nueva información
                nuevo_contrato = ContratoAlquiler(nuevo_arrendatario, nuevo_propiedad, nueva_fecha_inicio, nueva_fecha_fin, nueva_renta_mensual, nueva_fianza)

                gestor_contratos.modificar_contrato(indice_contrato, nuevo_contrato)
            else:
                print("Índice de contrato inválido.")
        elif opcion == "3":
                gestor_contratos.mostrar_contratos()
                indice_contrato = int(input("Ingrese el índice del contrato que desea eliminar: ")) - 1
                if 0 <= indice_contrato < len(gestor_contratos.contratos):
                    gestor_contratos.eliminar_contrato(indice_contrato)
                    print("Contrato eliminado exitosamente.")

                else:
                    print("Índice de contrato inválido.")

        elif opcion == "4":
            gestor_contratos.mostrar_contratos()
        elif opcion == "5":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 5.")

def menu_lista_tareas(lista_tareas):
    while True:
        print("\nMenú de Lista de Tareas:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como realizada")
        print("3. Mostrar lista de tareas")
        print("4. Eliminar tarea")
        print("5. Volver al menú principal")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            indice = int(input("Ingrese el índice de la tarea a marcar como realizada: ")) - 1
            lista_tareas.marcar_como_realizada(indice)
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        elif opcion == "4":
            indice = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
            lista_tareas.eliminar_tarea(indice)
        elif opcion == "5":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 5.")

def menu_gestion_documentos(gestion_documentos):
    while True:
        print("\nMenú de Gestión de Documentos:")
        print("1. Almacenar documento")
        print("2. Descargar documento")
        print("3. Mostrar lista de documentos")
        print("4. Volver al menú principal")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del documento: ")
            contenido = input("Ingrese el contenido del documento: ")
            gestion_documentos.almacenar_documento(nombre, contenido)
        elif opcion == "2":
            nombre_documento = input("Ingrese el nombre del documento que desea descargar: ")
            documento = gestion_documentos.descargar_documento(nombre_documento)
            if documento:
                print(f"Contenido del documento {nombre_documento}: {documento}")
            else:
                print("El documento especificado no existe.")
        elif opcion == "3":
            print("Lista de documentos almacenados:")
            for documento in gestion_documentos.documentos:
                print(documento.nombre)
        elif opcion == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 4.")


def mostrar_menu():
    print("\nMenú de Usuario:")
    print("1. Registrar nuevo usuario")
    print("2. Borrar usuario existente")
    print("3. Modificar información de usuario")
    print("4. opciones de contrato")
    print("5. Realizar pago de renta")
    print("6. Notificar incidencia")
    print("7. Lista de Tareas")
    print("8. Documentos")
    print("9. Salir")

def main():
    usuarios = []
    propiedades = []
    gestor_contratos = GestorContratos()
    lista_tareas = ListaTareas()
    gestion_documentos = GestionDocumentos()

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
            menu_gestor_contratos(gestor_contratos)
        elif opcion == "5":
            fecha_pago = datetime.datetime.now()
            importe = float(input("Ingrese el importe del pago de renta: "))
            pago_renta = PagoRenta(fecha_pago, importe)
            print("Pago de renta realizado exitosamente.")
        elif opcion == "6":
            # Notificar incidencia
            descripcion = input("Describa la incidencia: ")
            fecha_incidencia = datetime.datetime.now()
            incidencia = Incidencia(descripcion, fecha_incidencia, "Pendiente")
            print("Incidencia notificada correctamente.")
        elif opcion == "7":
            menu_lista_tareas(lista_tareas)
        elif opcion == "8":
            menu_gestion_documentos(gestion_documentos)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 9.")

if __name__ == "__main__":
    main()
