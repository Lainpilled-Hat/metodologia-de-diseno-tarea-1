import repositorio
from abc import ABC, abstractmethod

class Alumnos(ABC):
    @abstractmethod
    def __init__(self, rut, nombre, fecNac):
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
    def __init__(self, rut, nombre, fecNac):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.tipo = "Ayudante"
    def getRut(self):
        return self.rut
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
    def __init__(self, rut, nombre, fecNac):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.tipo = "Doctorado"
    def getRut(self):
        return self.rut
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
    def __init__(self, rut, nombre, fecNac):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.tipo = "Magister"
    def getRut(self):
        return self.rut
    @classmethod
    def estudiarMag():
        pass
    @classmethod
    def clases():
        pass
class Alumni(Alumnos):
    def __init__(self, rut, nombre, fecNac):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.tipo = "Alumni"
    def getRut(self):
        return self.rut
class NoAyudante(Pregrado):
    def __init__(self, rut, nombre, fecNac):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.tipo = "No Ayudante"
    def getRut(self):
        return self.rut
    def estudiar():
        pass