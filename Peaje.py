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
                print("Peaje creado correctamente.")
        except IntegrityError:
            print("Error: No se pudo crear el peaje debido a una violación de restricción única.")

def consultar_peaje(peaje_aconsultar):
    with psql_db.atomic():
        try:
            peaje_querido = peaje.select().where(peaje.nombre == peaje_aconsultar)
            print("Nombre: " + peaje_querido.nombre, "Ruta: " + peaje_querido.ruta, "Km: " + peaje_querido.km, "Telefono: " + peaje_querido.telefono_admin)
        except:
            print("Error: No se pudo consultar el peaje debido a una violación de restricción única.")
