from main import *
from Tablas import *
from Config import *
from Peaje import *

def ingresar_ventanilla(nombre_p, numero_ventanilla, tiene_rfid):
    with psql_db.atomic():
        try:
            peaje_obj = peaje.get_or_none(peaje.nombre == nombre_p)
            if peaje_obj:
                ventanilla.create(nombre_peaje=nombre_p, nro=numero_ventanilla, tiene_rfid=tiene_rfid)
                psql_db.commit()
                print("Ventanilla creada correctamente.")
            else:
                print("El peaje especificado no existe.")
        except IntegrityError:
            psql_db.rollback()
            print("Error: No se pudo crear la ventanilla debido a una violación de restricción única.")

#HAY QUE ARREGLAR ESTO
def consultar_ventanilla(peaje_aconsultar, ventanilla_aconsultar):
    with psql_db.atomic():
        ventanilla_querida = ventanilla.get(peaje_aconsultar, ventanilla_aconsultar)
        if ventanilla_querida.tiene_rfid == 1:
            tiene = "Si"
        else:
            tiene = "No"
        print(f"Nombre: {ventanilla_querida.nombre_peaje}, Numero: {ventanilla_aconsultar.nro}, Tiene RFID: {tiene}")
        