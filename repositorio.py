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
    def modificarAsignatura(self, codigo):
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
    def modificarPorRut(self, rut):
        pass

class Repositorio(AbstractRepositorio):
    def __init__(self):
        self.alumnos = {}
        self.asignaturas = {}
    def nuevoAlumno(self, alumno):
        self.alumnos[alumno.getRut() : alumno]
    def nuevaAsignatura(self, asignatura):
        self.asignaturas[asignatura.getCodigo() : asignatura]
    def recuperarAsignatura(self, codigo):
        asignatura = self.asignaturas.get(codigo)
        return asignatura
    def recuperarAlumno(self, rut):
        alumno = self.alumnos.get(rut)
        return alumno
    def eliminarPorRut(self, rut):
        alumno = self.alumnos.pop(rut)
        del alumno
    def eliminarAsignatura(self, codigo):
        asignatura = self.asignaturas.pop(codigo)
        del asignatura
    