
from abc import ABC, abstractmethod
import logging

#Brayan Stiven Camelo Torres
#Brayan Stiven Pinzon Aguilar
#Grupo: 213023_150

# Configurar logs

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Excepciones

class ClienteError(Exception):
    pass

class ServicioError(Exception):
    pass

class ReservaError(Exception):
    pass


# Clase Abtracta persona

class Persona(ABC):

    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_datos(self):
        pass


# Cliente


class Cliente(Persona):

    def __init__(self, nombre, documento, correo):

        if not nombre.strip():
            raise ClienteError("Nombre vacío")

        if len(documento) < 5:
            raise ClienteError("Documento invalido")

        if "@" not in correo:
            raise ClienteError("Correo invalido")

        super().__init__(nombre, documento)

        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def mostrar_datos(self):
        return f"{self.nombre} - {self.documento}"


# Servicio Abstracto


class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if tarifa <= 0:
            raise ServicioError("Tarifa invalida")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass


# Servicios


class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return self.tarifa * horas

class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias):
        return self.tarifa * dias

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, horas):
        return self.tarifa * horas


# Reserva


class Reserva:

    def __init__(self, cliente, servicio, cantidad):

        if cantidad <= 0:
            raise ReservaError("Cantidad invalida")

        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.estado = "Pendiente"

    def procesar(self):

        try:
            costo = self.servicio.calcular_costo(self.cantidad)

        except Exception as e:
            raise ReservaError("Error procesando reserva") from e

        else:
            self.estado = "Confirmada"
            logging.info("Reserva confirmada")
            return costo

        finally:
            logging.info("Proceso finalizado")


# Listas


clientes = []
servicios = []
reservas = []
