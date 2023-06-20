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
                    
                    dni_prop = persona.select(persona.dni).where(propietario_tiene_vehiculo.matricula == matricula).join(propietario_tiene_vehiculo, on=(persona.id_propietario == propietario_tiene_vehiculo.id_propietario)) 
                    dni_pariente = persona_pariente.select(persona_pariente.dni_pariente).where(persona_pariente.dni == dni_prop)

                    if dni_pariente.scalar() is None:
                        cuenta_a_debitar = (propietario_tiene_vehiculo.select(cuenta.nro_cuenta).where(propietario_tiene_vehiculo.matricula == matricula).join(cuenta, on=(propietario_tiene_vehiculo.id_propietario == cuenta.id_propietario)))
                        cuenta_debito = cuenta.get_by_id(cuenta_a_debitar)
                    else:
                        jefe = persona.get_by_id(dni_pariente)
                        cuenta_debito = cuenta.get(id_propietario = jefe.id_propietario)
                    
                    debito.create(matricula = matricula,id_ventanilla = vent.id_ventanilla, fecha_hora_debito = fecha_hora_actual, importe_debito = tarifa_pasada, numero_cuenta = cuenta_debito.nro_cuenta)
                    saldo_pasado = cuenta_debito.saldo
                    monto_debitar = tarifa_pasada.scalar()
                    nuevo_saldo = int(saldo_pasado - monto_debitar)
                    cuenta_debito.saldo = nuevo_saldo
                    cuenta_debito.save()
                    db_conn['rdbms'].commit()
                    print('Debito exitoso.')
        except IntegrityError:
            db_conn['rdbms'].rollback()
            print("Error: No se pudo realizar la acreditación.")
    
