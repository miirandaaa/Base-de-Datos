from main import *
from Tablas import *
from Config import *
from peewee import *

def consultar_persona(persona_aconsultar):
    with psql_db.atomic():
        try:
            persona_querida = persona.get_by_id(persona_aconsultar)
            print(f"DNI: {persona_querida.dni} \nNombres: {persona_querida.nombres} \nApellidos: {persona_querida.apellidos} \nCelular: {persona_querida.celular} \nEmail: {persona_querida.email} \nDireccion: {persona_querida.direccion}")
        except IntegrityError():
            print("Error: No se pudo consultar la persona debido a una violación de restricción única.")
