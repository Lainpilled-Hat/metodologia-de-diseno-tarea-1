from abc import ABC, abstractmethod
import datetime as date
import repositorio as rp

class Alumnos(ABC):
    def __init__(self, rut, nombre, fecNac):
        __today = date.today()
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        __fecha = abs(fecNac - __today)
        self.edad = __fecha.years
        return self
    def getRut(self):
        return self.rut
class Pregrado(Alumnos):
    def __init__(self, rut, nombre, fecNac):
        self = super().__init__(rut, nombre, fecNac)
        self.asignaturas = tuple()
        return self
    def estudiar(self, codigo):
        pass
    def inscribirRamo(self, codigo):
        pass
class Postgrado(Alumnos):
    @abstractmethod
    def estudiar(self, asignatura):
        pass
    @abstractmethod
    def clases(self, asignatura):
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
    @abstractmethod        
    def estudiar(self, asignatura):
        pass
class Doctorado(AbstractDoctorado, AbstractMagister):
    def __init__(self, rut, nombre, fecNac):
        self = super().__init__(rut, nombre, fecNac)
        self.tipo = "Doctorado"
        self.asignaturas = tuple()
        return self
    @classmethod
    def estudiar(self, asignatura):
        pass
    @classmethod
    def clases(self, asignatura):
        pass
    @classmethod
    def investigar(self):
        pass
class Magister(AbstractMagister):
    def __init__(self, rut, nombre, fecNac):
        self = super().__init__(rut, nombre, fecNac)
        self.tipo = "Magister"
        self.asignaturas = tuple()
        return self
    def inscribirRamos(self, codigo):
        pass
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
    def estudiar(self, asignatura):
        pass