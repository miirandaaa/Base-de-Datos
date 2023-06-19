from Tablas import *
from Config import *
from Peaje import *

def ingresar_vehiculo(dni, matricula, tag_rfid, marca, modelo, color, tipo):
     with psql_db.atomic():
        try:
            if vehiculo.get_or_none(vehiculo.matricula == matricula):
                print("El vehiculo ingresado ya existe.")
            else:
                dueño = persona.get_or_none(persona.dni == dni)
                if dueño:
                    tipo_existe = tipo_vehiculo.get_or_none(tipo_vehiculo.tipo == tipo)
                    if tipo_existe:
                        dueño_id = dueño.id_propietario
                        vehiculo.create(matricula=matricula, tag_rfid=tag_rfid, marca=marca, modelo=modelo, color=color, tipo_vehiculo=tipo)
                        propietario_tiene_vehiculo.create(id_propietario=dueño_id, matricula=matricula)
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

def consultar_vehiuclo():
    with psql_db.atomic():
        try:
            vehiculo_aconsultar = int(input("Ingrese la matricula del vehiculo: "))
            vehiculo_querido = vehiculo.get_by_id(vehiculo_aconsultar)
            print(f"Matricula: {vehiculo_querido.matricula} \nTag RFID: {vehiculo_querido.tag_rfid} \nMarca: {vehiculo_querido.marca} \nModelo: {vehiculo_querido.modelo} \nColor: {vehiculo_querido.color} \nTipo Vehiculo: {vehiculo_querido.tipo_vehiculo}")
        except IntegrityError():
            print("Error: No se pudo consultar el vehiculo debido a una violación de restricción única.")

def eliminar_vehiculo():
    with psql_db.atomic():
        matricula = int(input("Ingrese la matricula del vehiculo que desea eliminar: "))
        try:
            v_eliminar = vehiculo.get_or_none(vehiculo.matricula == matricula)
            if v_eliminar:
                propietarios = propietario.select().join(propietario_tiene_vehiculo).where(propietario_tiene_vehiculo.matricula == matricula)
                for propietario_instance in propietarios:
                    count = propietario_tiene_vehiculo.select(fn.COUNT(propietario_tiene_vehiculo.id_propietario)).where(propietario_tiene_vehiculo.id_propietario == propietario_instance.id_propietario).scalar()
                    if count == 1:
                        propietario_instance.delete_instance(recursive=True) #chequear si la cuena es de el que pasa a ser pariente
                    else:
                        propietario_tiene_vehiculo.get(propietario_tiene_vehiculo.id_propietario == propietario_instance.id_propietario, propietario_tiene_vehiculo.matricula == matricula).delete_instance()
                v_eliminar.delete_instance(recursive=True)
                psql_db.commit()
                print("Vehiculo eliminado correctamente.")
        except IntegrityError():
            psql_db.rollback()
        
        