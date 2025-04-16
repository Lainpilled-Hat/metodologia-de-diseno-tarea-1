from abc import ABC, abstractmethod
from datetime import date

class Alumnos(ABC):
    def __init__(self, rut, nombre, fecNac, edad=None):
        __today = date.today()
        self.rut = rut
        self.nombre = nombre
        self.fecNac = fecNac
        self.edad = __today.year - fecNac.year - ((__today.month, __today.day) < (fecNac.month, fecNac.day))
    
    def getRut(self):
        return self.rut
    def getName(self):
        return self.nombre
class Pregrado(Alumnos):
    def __init__(self, rut, nombre, fecNac, asignaturas = None):
        self = super().__init__(rut, nombre, fecNac)
        self.asignaturas = tuple()
    def estudiar(self, codigo):
        pass
    def inscribirRamo(self, codigo, repositorio):
        asignatura = repositorio.recuperarAsignatura(codigo)
        if asignatura.tipo == self.tipo:
            self.asignaturas.append(asignatura)
class Postgrado(Alumnos):
    @abstractmethod
    def estudiar(self, asignatura):
        pass
    @abstractmethod
    def clases(self, asignatura):
        pass
    def inscribirRamo(self, codigo, repositorio):
        asignatura = repositorio.recuperarAsignatura(codigo)
        if asignatura.tipo == self.tipo:
            self.asignaturas.append(asignatura)
class Ayudante(Pregrado):
    tipo = "Ayudante"
    def __init__(self, rut, nombre, fecNac):
        super().__init__(rut, nombre, fecNac)
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
    tipo = "Doctorado"
    def __init__(self, rut, nombre, fecNac, asignaturas=None):
        super().__init__(rut, nombre, fecNac, None)
        self.asignaturas = tuple()
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
    tipo = "Magister"
    def __init__(self, rut, nombre, fecNac, asignaturas=None):
        super().__init__(rut, nombre, fecNac, None)
        self.asignaturas = tuple()
    @classmethod
    def estudiar(self):
        pass
    @classmethod
    def clases(self):
        pass
class Alumni(Alumnos):
    tipo = "Alumni"
    def __init__(self, rut, nombre, fecNac):
        super().__init__(rut, nombre, fecNac)
class NoAyudante(Pregrado):
    tipo = "No Ayudante"
    def __init__(self, rut, nombre, fecNac):
        super().__init__(rut, nombre, fecNac)