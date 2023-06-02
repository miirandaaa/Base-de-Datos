from main import *
from Tablas import *
from Config import *
from peewee import *

def ingresar_propietario(dni, nombres, apellidos, celular, email, direccion, matricula, tag_rfid, marca, modelo, color, tipo):
    with psql_db.atomic():
        try:
            if persona.get_or_none(persona.dni == dni) and vehiculo.get_or_none(vehiculo.matricula == matricula):
                print("El Propietario y el Vehiculo ingresados ya existen.")
            else:
                nuevo_prop = propietario.create(tipo_propietario="Persona")
                persona.create(dni=dni, id_propietario=nuevo_prop.id_propietario, nombres=nombres, apellidos=apellidos, celular=celular, email=email, direccion=direccion)
                vehiculo.create(matricula=matricula, tag_rfid=tag_rfid, marca=marca, modelo=modelo, color=color, tipo_vehiculo=tipo, id_propietario=nuevo_prop.id_propietario)
                print("Propietario y Vehiculo agregado correctamente.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo crear el propietario debido a una violación de restricción única.")

def consultar_propietario(id_prop):
    with psql_db.atomic():
        try:
            prop_querido = propietario.get_by_id(id_prop)
            print(f"ID Propietario: {prop_querido.id_propietario} \nTipo Propietario: {prop_querido.tipo_propietario}")
        except IntegrityError():
            print("Error: No se pudo consultar la persona debido a una violación de restricción única.")

