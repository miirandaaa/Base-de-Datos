from Config import *
from Tablas import *

def reporte_titular_y_vehiculos():
    with psql_db.atomic():
        try:
            union_prop_persona = persona.select().join(propietario_tiene_vehiculo).where(propietario_tiene_vehiculo.id_propietario == persona.id_propietario)
            print (union_prop_persona)
            #for i in reporte:
            #    print(f"DNI: {i['persona.dni']}\nNombres: {i['persona.nombres']}\nApellidos: {i['persona.apellidos']}\nCelular: {i['persona.celular']}\nDireccion: {i['persona.direccion']}\nMatricula: {i['vehiculo.matricula']}\nMarca: {i['vehiculo.marca']}\nModelo: {i['vehiculo.modelo']}\nColor: {i['vehiculo.color']}\n")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo consultar el reporte debido a una violación de restricción única.")