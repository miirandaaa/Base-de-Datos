from main import *
from Tablas import *
from Config import *

def ingresar_peaje(nombre_peaje, ruta, km, telefono):
    with psql_db.atomic():
        peaje.create(nombre=nombre_peaje, ruta=ruta, km=km, telefono_admin=telefono)