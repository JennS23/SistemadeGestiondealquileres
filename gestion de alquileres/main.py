import datetime
import uuid

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Propiedad:
    def __init__(self, direccion, descripcion, numero_habitaciones, superficie, arrendador):
        self.direccion = direccion
        self.descripcion = descripcion
        self.numero_habitaciones = numero_habitaciones
        self.superficie = superficie
        self.arrendador = arrendador  # Nuevo atributo

class ContratoAlquiler:
    def __init__(self, usuario, propiedad, fecha_inicio, fecha_fin, renta_mensual, fianza, arrendador):
        self.id = uuid.uuid4()
        self.usuario = usuario
        self.propiedad = propiedad
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.renta_mensual = renta_mensual
        self.fianza = fianza
        self.arrendador = arrendador  # Nuevo atributo

class PagoRenta:
    def __init__(self, contrato, fecha_pago, importe):
        self.id = uuid.uuid4()
        self.contrato = contrato
        self.fecha_pago = fecha_pago
        self.importe = importe

class Incidencia:
    def __init__(self, contrato, descripcion, fecha, estado):
        self.id = uuid.uuid4()
        self.contrato = contrato
        self.descripcion = descripcion
        self.fecha = fecha
        self.estado = estado

class Documento:
    def __init__(self, contrato, nombre_archivo, tipo_archivo, contenido, arrendador):
        self.id = uuid.uuid4()
        self.contrato = contrato
        self.nombre_archivo = nombre_archivo
        self.tipo_archivo = tipo_archivo
        self.contenido = contenido
        self.arrendador = arrendador  # Nuevo atributo

def generar_id_pago():
    return uuid.uuid4()

def generar_id_incidencia():
    return uuid.uuid4()

def generar_id_documento():
    return uuid.uuid4()

def calcular_diferencia_fechas(fecha_inicio, fecha_fin):
    return (fecha_fin - fecha_inicio).days

def enviar_notificacion(nombre_usuario, asunto, mensaje):
    # Este es un ejemplo simple que imprime las notificaciones en la consola
    print(f"Notificación para {nombre_usuario}: {asunto} - {mensaje}")

class SistemaGestionAlquileres:
    def __init__(self):
        self.usuarios = []
        self.propiedades = []
        self.contratos_alquiler = []
        self.pagos_renta = []
        self.incidencias = []
        self.documentos = []

    def registrar_usuario(self, nombre):
        nuevo_usuario = Usuario(nombre)
        self.usuarios.append(nuevo_usuario)
        return nuevo_usuario

    def registrar_propiedad(self, direccion, descripcion, numero_habitaciones, superficie, arrendador):
        nueva_propiedad = Propiedad(direccion, descripcion, numero_habitaciones, superficie, arrendador)
        self.propiedades.append(nueva_propiedad)
        return nueva_propiedad

    def visualizar_contrato_alquiler(self, contrato_id):
        contrato = next((c for c in self.contratos_alquiler if c.id == contrato_id), None)
        if not contrato:
            raise ValueError("Contrato no encontrado")
        print(f"Información del contrato:")
        print(f"Usuario: {contrato.usuario.nombre}")
        print(f"Propiedad: {contrato.propiedad.direccion}")
        print(f"Fecha inicio: {contrato.fecha_inicio.strftime('%d/%m/%Y')}")
        print(f"Fecha fin: {contrato.fecha_fin.strftime('%d/%m/%Y')}")
        print(f"Renta mensual: {contrato.renta_mensual}")
        print(f"Fianza: {contrato.fianza}")

    def crear_contrato_alquiler(self, usuario, propiedad, fecha_inicio, fecha_fin, renta_mensual, fianza):
        nuevo_contrato = ContratoAlquiler(usuario, propiedad, fecha_inicio, fecha_fin, renta_mensual, fianza, propiedad.arrendador)
        self.contratos_alquiler.append(nuevo_contrato)
        return nuevo_contrato

    def registrar_pago_renta(self, contrato, fecha_pago, importe):
        nuevo_pago = PagoRenta(contrato, fecha_pago, importe)
        self.pagos_renta.append(nuevo_pago)
        # Enviar notificación al usuario del pago registrado
        enviar_notificacion(contrato.usuario.nombre, "Pago de renta registrado", f"Se ha registrado un pago de {importe} el {fecha_pago.strftime('%d/%m/%Y')}")

    def registrar_incidencia(self, contrato, descripcion, fecha, estado="pendiente"):
        nueva_incidencia = Incidencia(contrato, descripcion, fecha, estado)
        self.incidencias.append(nueva_incidencia)
        # Enviar notificación al arrendador sobre la incidencia
        enviar_notificacion(contrato.propiedad.arrendador, "Nueva incidencia registrada", f"Se ha registrado una incidencia: {descripcion}")

    def almacenar_documento(self, contrato, nombre_archivo, tipo_archivo, contenido):
        nuevo_documento = Documento(contrato, nombre_archivo, tipo_archivo, contenido, contrato.arrendador)
        self.documentos.append(nuevo_documento)
        # Enviar notificación al usuario sobre el nuevo documento almacenado
        enviar_notificacion(contrato.usuario.nombre, "Nuevo documento almacenado", f"Se ha almacenado un nuevo documento: {nombre_archivo}")

