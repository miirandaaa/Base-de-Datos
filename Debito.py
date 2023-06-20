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

            if vehiculo.get_or_none(vehiculo.matricula == matricula):
                id_peaje = int(input('Ingrese id peaje '))
                nro_ventanilla = int(input('Ingrese numero ventanilla '))
                vent = ventanilla.get(id_peaje = id_peaje, nro_ventanilla = nro_ventanilla)
                check = ventanilla.get_or_none(ventanilla.id_ventanilla == vent.id_ventanilla)
                if check:
                    vehiculo_pasada = vehiculo.get_by_id(matricula)
                    tarifa_pasada = tarifa.select(tarifa.valor).where((tarifa.tipo_vehiculo == vehiculo_pasada.tipo_vehiculo) & (tarifa.fecha_vigencia <= fecha_actual)).limit(1)
                    cuenta_a_debitar = (propietario_tiene_vehiculo.select(cuenta.nro_cuenta).where(propietario_tiene_vehiculo.matricula == matricula).join(cuenta, on=(propietario_tiene_vehiculo.id_propietario == cuenta.id_propietario)))
                    debito.create(matricula = matricula,id_ventanilla = vent.id_ventanilla, fecha_hora_debito = fecha_hora_actual, importe_debito = tarifa_pasada, numero_cuenta = cuenta_a_debitar)
                    
                    cuenta_debito = cuenta.get_by_id(cuenta_a_debitar)
                    saldo_pasado = cuenta_debito.saldo
                    nuevo_saldo = int(saldo_pasado - tarifa_pasada)
                    cuenta_debito.saldo = nuevo_saldo
                    cuenta_debito.save()
                    db_conn['rdbms'].commit()
                    print('Debito exitoso.')
        except IntegrityError:
            db_conn['rdbms'].rollback()
            print("Error: No se pudo realizar la acreditación.")
    
