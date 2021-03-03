from lector import Lector
from prestamo import Prestamo
from libro import Libro


lector1 = Lector(1, 'Antonio Fernando', 'Román Fernández')
libro1 = Libro('100', 'El arca de noe', 'Julio salinas', 'Alianz')
prestamo1 = Prestamo(lector1, libro1)
prestamo1.set_fecha_devolucion(2021, 3, 15)
print(f'El lector {lector1.nombre()} {lector1.apellidos()} es moroso: {lector1.moroso()}')


lector2 = Lector(2, 'Cristina', 'Marquez Rizo')
libro2 = Libro('101', 'El arca de noe', 'Julio salinas', 'Alianz')
prestamo2 = Prestamo(lector2, libro2)
prestamo2.set_fecha_devolucion(2021, 3, 27)
print(f'El lector {lector2.nombre()} {lector2.apellidos()} es moroso: {lector2.moroso()}')



lector3 = Lector(3, 'Adrian', 'Marquez Rizo')
libro3 = Libro('102', 'El arca de noe', 'Julio salinas', 'Alianz')
prestamo3 = Prestamo(lector3, libro2)
prestamo3.set_fecha_devolucion(2021, 3, 27)
print(f'El lector {lector3.nombre()} {lector3.apellidos()} es moroso: {lector3.moroso()}')
