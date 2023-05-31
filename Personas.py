from main import *
from Tablas import *
from Config import *
from peewee import *

def ingresar_persona_propietario(id_prop, dni, nombres, apellidos, celular, email, direccion):
     with psql_db.atomic():
        try:
            if persona.get_or_none(persona.dni == dni):
                print("La persona ingresada ya existe.")
            else:
                propietario.create(id_propietario=id_prop, tipo_propietario="persona")
                persona.create(dni=dni, id_propietario=id_prop, nombres=nombres, apellidos=apellidos, celular=celular, email=email, direccion=direccion)
                psql_db.commit()
                print("Persona agregada correctamente.")
        except IntegrityError:
            psql_db.rollback()
            print("Error: No se pudo crear la persona debido a una violación de restricción única.")

def consultar_persona(persona_aconsultar):
    with psql_db.atomic():
        try:
            persona_querida = persona.get_by_id(persona_aconsultar)
            print(f"DNI: {persona_querida.dni} \nNombres: {persona_querida.nombres} \nApellidos: {persona_querida.apellidos} \nCelular: {persona_querida.celular} \nEmail: {persona_querida.email} \nDireccion: {persona_querida.direccion}")
        except:
            print("Error: No se pudo consultar la persona debido a una violación de restricción única.")
