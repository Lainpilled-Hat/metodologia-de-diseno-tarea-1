from abc import ABC, abstractmethod
import datetime as date

class Alumnos(ABC):
    def __init__(self, rut, nombre, fecNac):
        _today = date.today()
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        _fecha = abs(fecNac - _today)
        self.edad = _fecha.years
        return self
    def getRut(self):
        return self.rut
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
        self = super().__init__(rut, nombre, fecNac)
        self.tipo = "Ayudante"
        return self
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
    def __init__(self, rut, nombre, fecNac):
        self = super().__init__(rut, nombre, fecNac)
        self.tipo = "Doctorado"
        return self
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
    def __init__(self, rut, nombre, fecNac):
        self = super().__init__(rut, nombre, fecNac)
        self.tipo = "Magister"
        return self
    @classmethod
    def estudiar(self):
        pass
    @classmethod
    def clases(self):
        pass
class Alumni(Alumnos):
    def __init__(self, rut, nombre, fecNac):
        self = super().__init__(rut, nombre, fecNac)
        self.tipo = "Alumni"
        return self
class NoAyudante(Pregrado):
    def __init__(self, rut, nombre, fecNac):
        self = super().__init__(rut, nombre, fecNac)
        self.tipo = "No Ayudante"
        return self
    def estudiar(self):
        pass