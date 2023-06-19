from Config import *
from Tablas import *

def reporte_titular_y_vehiculos():
    with psql_db.atomic():
        reportes = (vehiculo
            .select(vehiculo, propietario_tiene_vehiculo, persona)
            .join(propietario_tiene_vehiculo)
            .join(persona, on=(persona.id_propietario == propietario_tiene_vehiculo.id_propietario))
            .dicts())

        resultado = reportes.execute()
        fila_pasada = None
        for fila in resultado:
            if fila_pasada is None or fila.get('id_propietario') != fila_pasada.get('id_propietario'):
                print(f"Propietario: {fila.get('dni')} {fila.get('nombres')} {fila.get('apellidos')} {fila.get('celular')} {fila.get('direccion')} \nVehiculo: {fila.get('matricula')} {fila.get('marca')} {fila.get('modelo')} {fila.get('color')}")
                fila_pasada = fila
            else:
                print(f"Vehiculo: {fila.get('matricula')} {fila.get('marca')} {fila.get('modelo')} {fila.get('color')}")

def listado_cuenta_con_titular_y_vehiculos():
   with psql_db.atomic():
    reportes = (cuenta
                .select(cuenta, propietario, vehiculo)
                .join(propietario, on=(propietario.id_propietario == cuenta.id_propietario))
                .join(propietario_tiene_vehiculo, on=(propietario_tiene_vehiculo.id_propietario == propietario.id_propietario))
                .join(vehiculo, on=(vehiculo.matricula == propietario_tiene_vehiculo.matricula))
                .dicts())

    resultado = reportes.execute()
    cuenta_pasada = None
    for fila in resultado:
        if cuenta_pasada is None or fila.get('nro_cuenta') != cuenta_pasada.get('nro_cuenta'):
            print(f"Titular: {fila.get('id_propietario')} \nCuenta: {fila.get('nro_cuenta')} {fila.get('saldo')} {fila.get('fecha_creacion_cuenta')}")
            cuenta_pasada = fila
        print(f"Vehiculo: {fila.get('matricula')} {fila.get('marca')} {fila.get('modelo')}")


