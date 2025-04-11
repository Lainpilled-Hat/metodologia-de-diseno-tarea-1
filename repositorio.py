from abc import ABC, abstractmethod
class Repositorio(ABC):

    @abstractmethod
    def __init__(self, nombre, codigo, creditos):
        pass
    @abstractmethod
    def eliminarAsignatura(codigo):
        pass
    @abstractmethod
    def modificarAsignatura(codigo):
        pass
