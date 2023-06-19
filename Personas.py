from Tablas import *
from Config import *
from peewee import *
db_conn['rdbms'] = db_conn['rdbms']

def consultar_persona():
    with db_conn['rdbms'].atomic():
        try:
            persona_aconsultar = int(input("Ingrese el dni de la persona: "))
            persona_querida = persona.get_by_id(persona_aconsultar)
            print(f"DNI: {persona_querida.dni} \nID: {persona_querida.id_propietario} \nNombres: {persona_querida.nombres} \nApellidos: {persona_querida.apellidos} \nCelular: {persona_querida.celular} \nEmail: {persona_querida.email} \nDireccion: {persona_querida.direccion}")
        except IntegrityError():
            print("Error: No se pudo consultar la persona debido a una violación de restricción única.")

def modificar_persona(key, modificar, opcion):
    with db_conn['rdbms'].atomic():
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
                db_conn['rdbms'].commit()
            else:
                print("La persona no existe.")
        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo modificar la persona debido a una violación de restricción única.")
def eliminar_persona():
    with db_conn['rdbms'].atomic():
        try:
            persona_aeliminar = int(input("Ingrese el dni de la persona que desea eliminar: "))
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
                vehiculos = vehiculo.select().join(propietario_tiene_vehiculo).where(propietario_tiene_vehiculo.id_propietario == id_prop)
                for vehiculo_instance in vehiculos:
                    vehiculo_instance.delete_instance(recursive=True)
                id_prop.delete_instance(recursive = True)
                db_conn['rdbms'].commit()
                print("Persona eliminada correctamente.")
            else:
                print("La persona no existe.")
        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo eliminar la persona debido a una violación de restricción única.")