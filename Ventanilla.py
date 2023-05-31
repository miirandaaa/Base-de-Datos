from main import *
from Tablas import *
from Config import *
from Peaje import *

def ingresar_ventanilla(nombre_p, numero_ventanilla, tiene_rfid):
    with psql_db.atomic():
        peaje_obj = peaje.get_or_none(peaje.nombre == nombre_p)
        if peaje_obj:
            ventanilla.create(nombre_peaje=nombre_p, nro=numero_ventanilla, tiene_rfid=tiene_rfid)
            print("Ventanilla creada correctamente.")
        else:
            print("El peaje especificado no existe.")