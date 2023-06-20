from Tablas import *
from Config import *
from Cuenta import *
from datetime import datetime

def debito():
    with db_conn['rdbms'].atomic():
        try:
            fecha_hora_actual = datetime.now()
            fecha_actual = datetime(fecha_hora_actual.year, fecha_hora_actual.month, fecha_hora_actual.day,0,0)
            bonificacion = 10
            matricula = int(input('Ingrese matricula del vehiculo'))
            if vehiculo.get_or_none(vehiculo.matricula == matricula):
                vehiculo_pasada = vehiculo.get_by_id(vehiculo.matricula == matricula)
                tarifa_pasada = tarifa.select(tarifa.valor).where(tarifa.tipo_vehiculo == vehiculo_pasada.tipo_vehiculo and tarifa.fecha_vigencia >= fecha_actual)
                print(tarifa_pasada)
                print('Debito exitoso.')

        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo realizar la acreditación.")
    
