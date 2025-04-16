
import repositorio as rp
from abc import ABC, abstractmethod
class Asignatura(ABC):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        return self
    def getCodigo(self):
        return self.codigo

class AsignaturaPregrado(Asignatura):
    def __init__(self, nombre, codigo, creditos):
        self = super._init__(self,nombre, codigo, creditos)
        self.tipo = "Pregrado"
        return self
class AsignaturaMagister(Asignatura):
    def __init__(self, nombre, codigo, creditos):
        self = super._init__(self,nombre, codigo, creditos)
        self.tipo = "Magister"
        return self
class AsignaturaDoctorado(Asignatura):
    def __init__(self, nombre, codigo, creditos):
        self = super._init__(self,nombre, codigo, creditos)
        self.tipo = "Doctorado"
        return self