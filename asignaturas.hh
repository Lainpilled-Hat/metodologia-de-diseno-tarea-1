#pragma once
#include <iostream>
#include <sstream>
#include <string>


class Asignatura{
    public:
    int codigo;
    std::string nombre;
    int creditos;
    Asignatura crearPorAsignatura(std::string nombre, int codigo, int creditos);
    void eliminarPorCodigo(int codigo);
    Asignatura recuperarPorCodigo(int codigo);
    Asignatura modificarPorCodigo(int codigo);
    private:
    
};