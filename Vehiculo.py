from main import *
from Tablas import *
from Config import *
from Peaje import *

def ingresar_vehiculo(matricula, tag_rfid, marca, modelo, color, tipo):
     with psql_db.atomic():
        try:
            if vehiculo.get_or_none(vehiculo.matricula == matricula):
                print("El vehiculo ingresado ya existe.")
            else:
                tipo_existe = tipo_vehiculo.get_or_none(tipo_vehiculo.tipo == tipo)
                if tipo_existe:
                    vehiculo.create(matricula=matricula, tag_rfid=tag_rfid, marca=marca, modelo=modelo, color=color, tipo_vehiculo=tipo)
                    psql_db.commit()
                    print("Vehiculo creado correctamente.")
                else:
                    print("El tipo de vehiculo ingresado no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo crear el vehiculo debido a una violación de restricción única.")

def modificar_vehiculo(key, modificar, opcion):
    with psql_db.atomic():
        try:
            if vehiculo.get_or_none(vehiculo.matricula == key):
                v_mod = vehiculo.get(vehiculo.matricula == key)
                if opcion == 1:
                    v_mod.tag_rfid = modificar
                if opcion == 2:
                    v_mod.marca = modificar
                if opcion == 3:
                    v_mod.modelo = modificar
                if opcion == 4:
                    v_mod.color = modificar
                if opcion == 5:
                    if tipo_vehiculo.get_or_none(tipo_vehiculo.tipo == modificar):
                        v_mod.tipo_vehiculo = modificar
                v_mod.save()
                psql_db.commit()
            else:
                print("El vehiculo ingresado no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo modificar el vehiculo debido a una violación de restricción única.")
def consultar_vehiuclo(vehiculo_aconsultar):
    with psql_db.atomic():
        try:
            vehiculo_querido = vehiculo.get_by_id(vehiculo_aconsultar)
            print(f"Matricula: {vehiculo_querido.matricula} \nTag RFID: {vehiculo_querido.tag_rfid} \nMarca: {vehiculo_querido.marca} \nModelo: {vehiculo_querido.modelo} \nColor: {vehiculo_querido.color} \nTipo Vehiculo: {vehiculo_querido.tipo_vehiculo}")
        except IntegrityError():
            print("Error: No se pudo consultar el vehiculo debido a una violación de restricción única.")
            
def eliminar_vehiculo(vehiculo_aeliminar):
    with psql_db.atomic():
        propietario_querido = propietario_tiene_vehiculo.get_by_id(vehiculo_aeliminar)
        Query = propietario_tiene_vehiculo.select(fn.COUNT(propietario_tiene_vehiculo.vehiculo_aeliminiar.matricula)).where(propietario_tiene_vehiculo.id_propietario == propietario_querido.id_propietario)
        count = Query.scalar()
        print(count)
        if 
        sdsd
        try:
            vehiculo_querido = vehiculo.get_by_id(vehiculo_aeliminar)
            vehiculo_querido.delete()
            print("Vehiculo eliminado correctamente.")
        except IntegrityError():
            print("Error: No se pudo eliminar el vehiculo debido a una violación de restricción única.")