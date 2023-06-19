from Config import *
from Tablas import *

def reporte_titular_y_vehiculos():
    with psql_db.atomic():
        reportes = (vehiculo
            .select(vehiculo, propietario_tiene_vehiculo, persona)
            .join(propietario_tiene_vehiculo)
            .join(persona, on=(persona.id_propietario == propietario_tiene_vehiculo.id_propietario))
            .dicts())

        results = reportes.execute()
        for row in results:
            print(f"Propietario: {row.get('dni')} {row.get('nombres')} {row.get('apellidos')} \nVehiculo: {row.get('matricula')} {row.get('marca')} {row.get('modelo')} {row.get('color')} {row.get('tipo_vehiculo')}")
            print(row)