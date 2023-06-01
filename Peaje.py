from main import *
from Tablas import *
from Config import *
from peewee import *

def ingresar_peaje(nombre_peaje, ruta, km, telefono):
     with psql_db.atomic():
        try:
            if peaje.get_or_none(peaje.nombre == nombre_peaje):
                print("El peaje ingresado ya existe.")
            else:
                peaje.create(nombre=nombre_peaje, ruta=ruta, km=km, telefono_admin=telefono)
                psql_db.commit()
                print("Peaje creado correctamente.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo crear el peaje debido a una violación de restricción única.")

def consultar_peaje(peaje_aconsultar):
    with psql_db.atomic():
        try:
            peaje_querido = peaje.get_by_id(peaje_aconsultar)
            print(f"Nombre: {peaje_querido.nombre} \nRuta: {peaje_querido.ruta} \nKm: {peaje_querido.km} \nTelefono: {peaje_querido.telefono_admin}")
        except IntegrityError():
            print("Error: No se pudo consultar el peaje debido a una violación de restricción única.")

def modificar_peaje(key, modifcar, opcion): #Preguntar si se modifica solo el nombre dos atributos todos como es
    with psql_db.atomic():
        try:
            if peaje.get_or_none(peaje.nombre == key):
                p_mod = peaje.get(peaje.nombre == key)
                if opcion == 1:
                    p_mod.ruta = modifcar
                if opcion == 2:
                    p_mod.km = modifcar
                if opcion == 3:
                    p_mod.telefono_admin = modifcar
                p_mod.save()
                psql_db.commit()
            else:
                print("El peaje ingresado no existe.")
        except:
            psql_db.rollback()
            print("Error: No se pudo modificar el peaje debido a una violación de restricción única.")
