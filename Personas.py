from main import *
from Tablas import *
from Config import *
from peewee import *

def ingresar_persona_propietario(dni, nombres, apellidos, celular, email, direccion):
     with psql_db.atomic():
        try:
            if persona.get_or_none(persona.dni == dni):
                print("La persona ingresada ya existe.")
            else:
                propietario.create(tipo_propietario="persona")
                persona.create(dni=dni, nombres=nombres, apellidos=apellidos, celular=celular, email=email, direccion=direccion)
                print("Persona agregada correctamente.")
        except IntegrityError:
            print("Error: No se pudo crear la persona debido a una violación de restricción única.")
    #metodos a implementar agregar persona y propietario y vehiculo
