
import repositorio as rp
from abc import ABC, abstractmethod
class Asignatura(ABC):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
    def getCodigo(self):
        return self.codigo
    def getNombre(self):
        return self.nombre
    def getCreditos(self):
        return self.creditos

class AsignaturaPregrado(Asignatura):
    tipo = "Pregrado"
    def __init__(self, nombre, codigo, creditos):
        super._init__(self,nombre, codigo, creditos)
    def getTipo(self):
        return self.tipo
class AsignaturaMagister(Asignatura):
    tipo = "Magister"
    def __init__(self, nombre, codigo, creditos):
        super._init__(self,nombre, codigo, creditos)
    def getTipo(self):
        return self.tipo

class AsignaturaDoctorado(Asignatura):
    tipo = "Doctorado"
    def __init__(self, nombre, codigo, creditos):
        super._init__(self,nombre, codigo, creditos)
    def getTipo(self):
        return self.tipo