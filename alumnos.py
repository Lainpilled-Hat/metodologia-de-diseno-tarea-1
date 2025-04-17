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
    def getEdad(self):
        return self.edad
    def getFechaNacimiento(self):
        return self.fecNac
class Pregrado(Alumnos):
    def __init__(self, rut, nombre, fecNac, asignaturas = None, creditos = 0):
        super().__init__(rut, nombre, fecNac, None)
        self.asignaturas = tuple()
    def estudiar(self, codigo, repositorio):
        asignatura = repositorio.recuperarAsignatura(codigo)
        if asignatura.getTipo() == "Pregrado":
            print("El estudiante", self.getName(), "va a estudiar", asignatura.getNombre())
        else:
            print("Esta asignatura no corresponde al tipo de estudiante")
    def inscribirRamo(self, codigo, repositorio):
        asignatura = repositorio.recuperarAsignatura(codigo)
        if asignatura.tipo == self.tipo and (asignatura.getCreditos() + self.creditos) <= 30:
            self.asignaturas.append(asignatura)
class Postgrado(Alumnos):
    @abstractmethod
    def estudiar(self, codigo, repositorio):
        pass
    @abstractmethod
    def clases(self, codigo, repositorio):
        pass
    def inscribirRamo(self, codigo, repositorio):
        asignatura = repositorio.recuperarAsignatura(codigo)
        if asignatura.tipo == self.tipo and (asignatura.getCreditos() + self.creditos) <= 30:
            self.asignaturas.append(asignatura)
class Ayudante(Pregrado):
    tipo = "Ayudante"
    def __init__(self, rut, nombre, fecNac, creditos = 0):
        super().__init__(rut, nombre, fecNac, None)
    def ayudantia(self, repositorio, codigo):
        asignatura = repositorio.recuperarAsignatura(codigo)
        print("El ayudante", self.getName(), "va a ser ayudante en la clase", asignatura.getNombre())
class AbstractDoctorado(Postgrado):
    @abstractmethod
    def investigar(self):
        pass
class AbstractMagister(Postgrado):
    @abstractmethod        
    def estudiar(self, asignatura, repositorio):
        pass
class Doctorado(AbstractDoctorado, AbstractMagister):
    tipo = "Doctorado"
    def __init__(self, rut, nombre, fecNac, asignaturas=None, cursos = None, creditos = 0):
        super().__init__(rut, nombre, fecNac, None)
        self.asignaturas = tuple()
    @classmethod
    def estudiar(self, codigo, repositorio):
        asignatura = repositorio.recuperarAsignatura(codigo)
        if asignatura.getTipo() == "Doctorado":
            print("El estudiante", self.getName(), "va a estudiar", asignatura.getNombre())
        else:
            print("Esta asignatura no corresponde al tipo de estudiante")
    @classmethod
    def clases(self, codigo, repositorio):
        pass
    @classmethod
    def investigar(self):
        pass
class Magister(AbstractMagister):
    tipo = "Magister"
    def __init__(self, rut, nombre, fecNac, asignaturas=None, cursos = None, creditos = 0):
        super().__init__(rut, nombre, fecNac, None)
        self.asignaturas = tuple()
        self.cursos = tuple()
    @classmethod
    def estudiar(self, codigo, repositorio):
        asignatura = repositorio.recuperarAsignatura(codigo)
        if asignatura.getTipo() == "Magister":
            print("El estudiante", self.getName(), "va a estudiar", asignatura.getNombre())
        else:
            print("Esta asignatura no corresponde al tipo de estudiante")
    @classmethod
    def clases(self, codigo, repositorio):
        pass
class Alumni(Alumnos):
    tipo = "Alumni"
    def __init__(self, rut, nombre, fecNac):
        super().__init__(rut, nombre, fecNac, None)
class NoAyudante(Pregrado):
    tipo = "No Ayudante"
    def __init__(self, rut, nombre, fecNac):
        super().__init__(rut, nombre, fecNac, None)