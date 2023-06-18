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

def modificar_persona(key, modificar, opcion):
    with psql_db.atomic():
        try:
            if persona.get_or_none(persona.dni == key):
                p_mod = persona.get(persona.dni == key)
                if opcion == 1:
                    p_mod.nombres = modificar
                if opcion == 2:
                    p_mod.apellidos = modificar
                if opcion == 3:
                    p_mod.celular = modificar
                if opcion == 4:
                    p_mod.email = modificar
                if opcion == 5:
                    p_mod.direccion = modificar    
                p_mod.save()
                print("Persona modificada correctamente.")
                psql_db.commit()
            else:
                print("La persona no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo modificar la persona debido a una violación de restricción única.")
def eliminar_persona(persona_aeliminar):
    with psql_db.atomic():
        try:
            p_eliminar = persona.get_or_none(persona.dni == persona_aeliminar)
            id_prop = p_eliminar.id_propietario
            if p_eliminar:
                cuenta_eliminar = cuenta.get_or_none(cuenta.id_propietario == id_prop)
                if cuenta_eliminar:
                    if persona_pariente.get_or_none(persona_pariente.dni == p_eliminar.dni):
                        p_pariente = persona.get_by_id(persona_pariente.dni_pariente)
                        cuenta_eliminar.id_propietario = p_pariente.id_propietario
                        cuenta_eliminar.save()
                    else:
                        cuenta_eliminar.delete_instance()
                id_prop.delete_instance(recursive = True)
                psql_db.commit()
                print("Persona eliminada correctamente.")
            else:
                print("La persona no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo eliminar la persona debido a una violación de restricción única.")