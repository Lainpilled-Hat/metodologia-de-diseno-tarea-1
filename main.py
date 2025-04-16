# Aquí va el main, hay que conectar los tres archivos aquí
import repositorio as rp
import alumnos as al
import asignaturas as ramo
from datetime import date

def __init__():
    repositorio = rp.Repositorio()
    fecha = date(2002,7,24)
    doctor = al.Doctorado("21073882-7", "Roberto Manfinfla", fecha)
    repositorio.nuevoAlumno(doctor)
    usuario = repositorio.recuperarPorRut("21073882-7")

__init__()