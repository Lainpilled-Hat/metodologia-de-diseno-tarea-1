class Alumnos{
    public:
        uint rut;
        string nombre;
        uint edad;
        datetime.date fechaNacimiento;
        datetime.date getFechaNacimiento(Alumnos alumno);
        Alumnos recuperarPorRut(string rut);
        int getEdad(Alumnos alumno);
        Alumnos crearAlumno(uint day, uint month, uint year, string name, string rut);
        void eliminarAlumno(Alumnos alumno);
        void modificarPorRut(string rut, data dato)
    private:
        string getName(Alumnos alumno);
        string getrut(Alumnos alumno);
        void setName(string nombre);
    ☻   void setRut(string rut);
        void setFechaNacimiento(uint day, uint month, uint year);
        datetime.year year;
        datetime.month month;
        datetime.day day;
        string getRutFull(uint rut);
}