
import repositorio as rp
from abc import ABC, abstractmethod
class Asignatura(ABC):
    @abstractmethod
    def __init__(self, nombre, codigo, creditos):
        pass
class AsignaturaPregrado(Asignatura):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = "Pregrado"
class AsignaturaMagister(Asignatura):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = "Magister"
class AsignaturaDoctorado(Asignatura):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = "Doctorado"
