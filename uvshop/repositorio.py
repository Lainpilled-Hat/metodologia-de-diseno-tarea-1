from abc import ABC, abstractmethod
from datetime import date

class RepositorioAbstracto(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def agregarMetodoPago(self, metodo):
        pass
    @abstractmethod
    def cancelarPedido(self, id):
        pass
    @abstractmethod
    def agredarPedido(self, pedido):
        pass
    @abstractmethod
    def agregarCliente(self, cliente):
        pass
    @abstractmethod
    def recuperarPedido(self,id):
        pass
class Repositorio(RepositorioAbstracto):
    def __init__(self):
        self.pedidos = {}
        self.clientes = {}
        self.metodosPago = {}
    def agregarCliente(self, cliente):
        email = cliente.getEmail()
    def recuperarPedido(self, id):
        pedido = self.pedidos.get(id)
        return pedido
        self.clientes.update({email: cliente})
    def agregarPedido(self, pedido):
        id = pedido.getId()
        self.pedidos.update({id: pedido})
    def cancelarPedido(self, id):
        pedido = recuperarPedido(self, id)