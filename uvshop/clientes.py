from abc import ABC, abstractmethod
from datetime import date

class Clientes(ABC):
    def __init__(self, nombre, email, direccion, tipo = None):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.tipo = tipo
    def getNombre(self):
        return self.nombre
    def getEmail(self):
        return self.email
    def getDireccion(self):
        return self.direccion
    def getTipo(self):
        return self.tipo
class Nuevo(Clientes):
    def __init__(self, nombre, email, direccion):
        super().__init__(self, nombre, email, direccion, "Nuevo")
        self.descuento = 0.05
        self.envio_gratis = False
class Frecuente(Clientes):
    def __init__(self, nombre, email, direccion):
        super().__init__(self, nombre, email, direccion, "Frecuente")
        self.descuento = 0.10
        self.envio_gratis = False
class VIP(Clientes):
    def __init__(self, nombre, email, direccion):
        super().__init__(self, nombre, email, direccion, "VIP")
        self.descuento = 0.15
        self.envio_gratis = True