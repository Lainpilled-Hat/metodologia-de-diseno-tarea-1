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
    @abstractmethod
    def nuevoAlumno(self, alumno):
        pass
    @abstractmethod
    def nuevaAsignatura(self, asignatura):
        pass
    @abstractmethod
    def inscribirAsignatura(self, asignatura, alumno):
        pass
class Repositorio(AbstractRepositorio):
    def __init__(self):
        self.repoAlumnos = {}
        self.repoAsignaturas = {}
        return self
    def nuevoAlumno(self, alumno):
        self.repoAlumnos[alumno.getRut() : alumno]
        return self
    def nuevaAsignatura(self, asignatura):
        self.repoAsignaturas[asignatura.getCodigo() : asignatura]
        return self
    def recuperarAsignatura(self, codigo):
        asignatura = self.repoAsignaturas.get(codigo)
        return asignatura
    def recuperarAlumno(self, rut):
        alumno = self.repoAsignaturas.get(rut)
        return alumno
    def eliminarPorRut(self, rut):
        alumno = self.repoAlumnos.pop(rut)
        del alumno
        return self
    def eliminarAsignatura(self, codigo):
        asignatura = self.repoAsignaturas.pop(codigo)
        del asignatura
        return self
    