from abc import ABC, abstractmethod
import alumnos, asignaturas
class AbstractRepositorio(ABC):

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def eliminarAsignatura(self, codigo):
        pass
    @abstractmethod
    def modificarAsignatura(self, codigo, nombre=None, creditos = None):
        pass
    @abstractmethod
    def recuperarAsignatura(self, codigo):
        pass
    @abstractmethod
    def recuperarPorRut(self, rut):
        pass
    @abstractmethod
    def eliminarPorRut(self, rut):
        pass
    @abstractmethod
    def modificarPorRut(self, rut, nombre = None, fecNac = None):
        pass
    @abstractmethod
    def nuevoAlumno(self, alumno):
        pass
    @abstractmethod
    def nuevaAsignatura(self, asignatura):
        pass
class Repositorio(AbstractRepositorio):
    def __init__(self):
        self.repoAlumnos = {}
        self.repoAsignaturas = {}
    def nuevoAlumno(self, alumno):
        rut = alumno.getRut()
        self.repoAlumnos.update({rut : alumno})
    def nuevaAsignatura(self, asignatura):
        codigo = asignatura.getCodigo()
        self.repoAsignaturas.update({codigo: asignatura})
    def recuperarAsignatura(self, codigo):
        asignatura = self.repoAsignaturas.get(codigo)
        return asignatura
    def modificarPorRut(self, rut, nombre = None, fecNac = None):
        alumno = self.repoAlumnos.pop(rut)
        if nombre != None:
            alumno.nombre = nombre
        if fecNac != None:
            alumno.fecNac = fecNac
        self.repoAlumnos.update(rut, alumno)
    def modificarAsignatura(self, codigo, nombre = None, creditos = None):
        asignatura = self.repoAsignaturas.pop(codigo)
        if nombre != None:
            asignatura.nombre = nombre
        if creditos != None:
            asignatura.creditos = creditos
        self.repoAsignaturas.update(codigo, asignatura)
    def recuperarPorRut(self, rut):
        alumno = self.repoAlumnos.get(rut)
        return alumno
    def eliminarPorRut(self, rut):
        alumno = self.repoAlumnos.pop(rut)
        del alumno
    def eliminarAsignatura(self, codigo):
        asignatura = self.repoAsignaturas.pop(codigo)
        del asignatura
    