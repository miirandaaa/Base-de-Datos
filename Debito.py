from Tablas import *
from Config import *
from Cuenta import *
from datetime import datetime

def debitar():
    with db_conn['rdbms'].atomic():
        try:
            fecha_hora_actual = datetime.now()
            fecha_actual = datetime(fecha_hora_actual.year,fecha_hora_actual.month,fecha_hora_actual.day,0,0)
            bonificacion = 10
            matricula = int(input('Ingrese matricula del vehiculo '))
            id_peaje = int(input('Ingrese id peaje '))
            nro_ventanilla = int(input('Ingrese numero ventanilla '))

            if vehiculo.get_or_none(vehiculo.matricula == matricula):
                if ventanilla.get_or_none(ventanilla.id_peaje == id_peaje, ventanilla.nro_ventanilla == nro_ventanilla):
                    print("Enero")
                    ventanilla_id = ventanilla.get(id_peaje = id_peaje,nro_ventanilla = nro_ventanilla)
                    print("Febrero")
                    vehiculo_pasada = vehiculo.get_by_id(matricula)
                    print("Marzo")
                    tarifa_pasada = tarifa.select(tarifa.valor).where(tarifa.tipo_vehiculo == vehiculo_pasada.tipo_vehiculo and tarifa.fecha_vigencia <= fecha_actual)
                    print("Abril")
                    debito.create
                    #cuenta_debitar = cuenta.join(propietario_tiene_vehiculo, on=(propietario_tiene_vehiculo.id_propietario == cuenta.id_propietario)).join(vehiculo, on=(vehiculo.matricula == matricula, propietario_tiene_vehiculo.matricula == vehiculo.matricula)).select(cuenta.nro_cuenta)
                    
                    db_conn['rdbms'].commit()
                    print('Debito exitoso.')

        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo realizar la acreditación.")
    
