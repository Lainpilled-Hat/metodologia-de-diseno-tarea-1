from abc import ABC, abstractmethod

class Alumnos(ABC):
    @abstractmethod
    def __init__(self, rut, nombre, fecNac, edad):
        pass
    def getRut(self):
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
    def __init__(self, rut, nombre, fecNac, edad):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.edad = edad
        self.tipo = "Ayudante"
    @classmethod
    def ayudantia(self):
        pass
class AbstractDoctorado(Postgrado):
    @abstractmethod
    def investigar(self):
        pass
class AbstractMagister(Postgrado):
        pass
class Doctorado(AbstractDoctorado, AbstractMagister):
    def __init__(self, rut, nombre, fecNac, edad):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.edad = edad
        self.tipo = "Doctorado"
    def getRut(self):
        return self.rut
    @classmethod
    def estudiar(self):
        pass
    @classmethod
    def clases(self):
        pass
    @classmethod
    def investigar(self):
        pass
class Magister(AbstractMagister):
    def __init__(self, rut, nombre, fecNac, edad):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.edad = edad
        self.tipo = "Magister"
    def getRut(self):
        return self.rut
    @classmethod
    def estudiar(self):
        pass
    @classmethod
    def clases(self):
        pass
class Alumni(Alumnos):
    def __init__(self, rut, nombre, fecNac, edad):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.edad = edad
        self.tipo = "Alumni"
    def getRut(self):
        return self.rut
class NoAyudante(Pregrado):
    def __init__(self, rut, nombre, fecNac, edad):
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.edad = edad
        self.tipo = "No Ayudante"
    def getRut(self):
        return self.rut
    def estudiar(self):
        pass