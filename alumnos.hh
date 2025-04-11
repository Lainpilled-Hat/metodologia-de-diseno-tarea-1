#pragma once
#include <iostream>
#include <ctime>
#include <sstream>
#include <string>


class Alumnos{
    public:
        int32_t rut;
        std::string nombre;
        int32_t year;
        int32_t month;
        int32_t day;
        Alumnos recuperarPorRut(std::string rut);
        time_t getFechaNacimiento(Alumnos alumno);
        int getEdad(Alumnos alumno);
        Alumnos crearAlumno(int day, int month, int year, std::string name, std::string rut);
        void eliminarAlumno(Alumnos alumno);
        template <typename data>
        void modificarPorRut(std::string rut, data dato);
    private:
        std::string getName(Alumnos alumno);
        std::string getrut(Alumnos alumno);
        void setName(std::string nombre);
        void setRut(std::string rut);
        void setFechaNacimiento(int day, int month, int year);
        std::string getRutFull(int rut);
};