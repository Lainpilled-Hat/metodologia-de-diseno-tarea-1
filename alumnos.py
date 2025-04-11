import repositorio
from abc import ABC, abstractmethod

class Alumnos(ABC):
    @abstractmethod
    def __init__(self, rut, nombre, fecNac):
        pass
    @abstractmethod
    def recuperarRut(rut):
        pass
    @abstractmethod
    def eliminarAlumnos(self):
        pass
    @abstractmethod
    def modificarAlumno(self):
        pass
class Pregrado(Alumnos):
    @abstractmethod
    def estudiar(self):
        pass
class Postgrado(Alumnos):
    @abstractmethod
    def estudiar(self):
        pass
    @abstractmethod
    def clases(self):
        pass
class Ayudante(Pregrado):
    @classmethod
    def estudiar(self):
        pass
    @classmethod
    def ayudantia(self):
        pass
class AbstractDoctorado(Postgrado):
    @abstractmethod
    def estudiarDoc(self):
        pass
    @abstractmethod
    def investigar(self):
        pass
class AbstractMagister(Postgrado):
    @abstractmethod
    def estudiarMag(self):
        pass
    @abstractmethod
    def clases(self):
        pass
class Doctorado(AbstractDoctorado, AbstractMagister):
    @classmethod
    def estudiarDoc():
        pass
    @classmethod
    def clases():
        pass
    @classmethod
    def investigar():
        pass
class Magister(AbstractMagister):
    @classmethod
    def estudiarMag():
        pass
    @classmethod
    def clases():
        pass
class Alumni(Alumnos):
    pass
class NoAyudante(Pregrado):
    pass