from main import *
from Tablas import *
from Config import *
from Peaje import *

def ingresar_vehiculo(matricula, tag_rfid, marca, color, tipo):
     with psql_db.atomic():
        try:
            if vehiculo.get_or_none(vehiculo.matricula == matricula):
                print("El vehiculo ingresado ya existe.")
            else:
                tipo_existe = tipo_vehiculo.get_or_none(tipo_vehiculo.tipo == tipo)
                if tipo_existe:
                    vehiculo.create(matricula=matricula, tag_rfid=tag_rfid, marca=marca, color=color, tipo_vehiculo=tipo)
                    print("Vehiculo creado correctamente.")
                else:
                    print("El tipo de vehiculo ingresado no existe.")
        except IntegrityError:
            print("Error: No se pudo crear el vehiculo debido a una violación de restricción única.")