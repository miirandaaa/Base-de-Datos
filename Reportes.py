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