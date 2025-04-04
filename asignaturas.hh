class Asignatura{
    public:
    uint codigo;
    string nombre;
    uint creditos;
    Asignatura crearPorAsignatura(string nombre, uint codigo, uint creditos);
    void eliminarPorCodigo(uint codigo);
    Asignatura recuperarPorCodigo(uint codigo);
    Asignatura modificarPorCodigo(uint codigo);
    private:
    
}