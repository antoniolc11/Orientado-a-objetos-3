from datetime import date

class Prestamo:

    __libros_alquilados = {}

    def __init__(self, lector, libro):
        if libro.codigo() in Prestamo.__libros_alquilados:
            raise NameError('El libro ya está alquilado')
        self.__lector = lector
        self.__libro = libro
        self.__fecha_prestamo = date.today()
        self.__fecha_devolucion = None
        Prestamo.__libros_alquilados[self.__libro.codigo()] = self

    def lector(self):
        return self.__lector

    def libro(self):
        return self.__libro

    def fecha_prestamo(self):
        return self.__fecha_prestamo


    def fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, año, mes, dia):
        """
        Recibe la fecha en la que se devuelve el libro,
        Elimina el libro de la clase __libros_alquilados, para que pueda ser alquilado.
        y comprueba el numero de días que ha estado alquilado, si ha sido mas de 15
        marca al lector como mororo utilizando el metodo: set_moroso() de la clase lector.

        set_fecha_devolucion(año, mes, dia) --> None
        """
        self.__fecha_devolucion = date(año, mes, dia)
        del Prestamo.__libros_alquilados[self.__libro.codigo()]
        dias_prestamo = (self.__fecha_devolucion - self.__fecha_prestamo).days
        if dias_prestamo > 15:
            self.__lector.set_moroso()

    @staticmethod
    def libros_alquilados():
        return Prestamo.__libros_alquilados
