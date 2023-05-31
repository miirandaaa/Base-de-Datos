from main import *
from Tablas import *
from Config import *
from Peaje import *

def ingresar_ventanilla(nombre_p, numero_ventanilla, tiene_rfid):
    with psql_db.atomic():
        try:
            if peaje.get_or_none(peaje.nombre == nombre_p):
                ventanilla.create(nombre_peaje=peaje, nro=numero_ventanilla, tiene_rfid=tiene_rfid)
                print("Ventanilla creada correctamente.")
            else:
                print("El peaje especificado no existe.")
        except IntegrityError:
            print("Error: No se pudo crear la ventanilla debido a una violación de restricción única.")