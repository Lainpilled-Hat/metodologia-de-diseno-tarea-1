from abc import ABC, abstractmethod
from datetime import date


# Estado = pendiente, pagado, en preparacion, enviado, entregado, cancelado
class Pedido(ABC):
    def __init__(self, id, nombre, codigo, precio, stock, prioridad):
        self.id = id #PK
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.stock = stock
        self.estado = "Pendiente"
        self.prioridad = prioridad

class Estandar(Pedido):
    def __init__(self, id, nombre, codigo, precio, stock):
        super().__init__(self, id, nombre, codigo, precio, stock, 0)
        
class Expres(Pedido):
    def __init__(self, id, nombre, codigo, precio, stock, prioridad):
        super().__init__(self, id, nombre, codigo, precio, stock, prioridad)
class Programado(Pedido):
    def __init__(self, id, nombre, codigo, precio, stock, prioridad, fecha):
        super().__init__(self, id, nombre, codigo, precio, stock, prioridad)
        self.fecha = fecha
class Internacional(Pedido):
    def __init__(self, id, nombre, codigo, precio, stock, prioridad, impuestos):
        super().__init__(self, id, nombre, codigo, precio, stock, prioridad)
        self.precio = precio * impuestos