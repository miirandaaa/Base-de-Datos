from Tablas import *
from Config import *
from Cuenta import *
from datetime import datetime
import datetime

def debito():
    with db_conn['rdbms'].atomic():
        try:
            fecha_hora_actual = datetime.now()
            fecha_actual = datetime.date(fecha_hora_actual.year,fecha_hora_actual.month,fecha_hora_actual.day,0,0)
            bonificacion = 10
            matricula = int(input('Ingrese matricula del vehiculo'))
            if vehiculo.get_or_none(vehiculo.matricula == matricula):
                vehiculo_pasada = vehiculo.get_by_id(vehiculo.matricula == matricula)
                tarifa_pasada = tarifa.select(tarifa.valor).where(tarifa.tipo_vehiculo == vehiculo_pasada.tipo_vehiculo and tarifa.fecha_vigencia >= fecha_actual)
                print(tarifa_pasada)

                cuenta_debitar = cuenta.join(propietario_tiene_vehiculo, on=(propietario_tiene_vehiculo.id_propietario == cuenta.id_propietario)).join(vehiculo, on=(vehiculo.matricula == matricula, propietario_tiene_vehiculo.matricula == vehiculo.matricula)).select(cuenta.nro_cuenta)
                print(cuenta_debitar)
                print('Debito exitoso.')

        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo realizar la acreditación.")
    
