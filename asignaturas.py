
import repositorio as rp
  
class AsignaturaPregrado(rp.Repositorio):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = "Pregrado"
    def eliminarAsignatura(codigo):
        pass
class AsignaturaMagister(rp.Repositorio):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = "Magister"
class AsignaturaDoctorado(rp.Repositorio):
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.tipo = "Doctorado"
