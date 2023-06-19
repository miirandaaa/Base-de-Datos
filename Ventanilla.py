from Tablas import *
from Config import *
from Peaje import *

def ingresar_ventanilla(nombre_p, nro, tiene_rfid):
    with psql_db.atomic():
        try:
            peaje_obj = peaje.get_or_none(peaje.nombre == nombre_p)
            peaje_id = peaje_obj.id_peaje
            if peaje_obj:
                ventanilla_obj = ventanilla.get_or_none(ventanilla.id_peaje == peaje_id, ventanilla.nro_ventanilla == nro)
                if ventanilla_obj == None:
                    ventanilla.create(id_peaje=peaje_id, nro_ventanilla = nro, tiene_rfid=tiene_rfid)
                    psql_db.commit()
                    print("Ventanilla creada correctamente.")
                else: 
                    print("La ventanilla ya existe.")
            else:
                print("El peaje especificado no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo crear la ventanilla debido a una violación de restricción única.")

def modificar_ventanilla(nombre,numero,RFID):
    with psql_db.atomic():
        try:
            peaje_obj = peaje.get_or_none(peaje.nombre == nombre)
            peaje_id = peaje_obj.id_peaje
            if peaje_obj:
                ventanilla_obj = ventanilla.get_or_none(ventanilla.id_peaje == peaje_id, ventanilla.nro_ventanilla == numero)
                if ventanilla_obj:
                    ventanilla_obj.tiene_rfid=RFID
                    ventanilla_obj.save()
                    psql_db.commit()
                    print("Ventanilla modificada correctamente.")
                else:
                    print("La ventanilla no existe.")
            else:
                print("El peaje no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo crear la ventanilla debido a una violación de restricción única.")

#falta hacer esto
def consultar_ventanilla():
    with psql_db.atomic():
        try:
            peaje_aconsultar = input("Ingrese el nombre del peaje: ")
            id_peaje = peaje.get(peaje.nombre == peaje_aconsultar).id_peaje
            ventanillas = ventanilla.select().where(ventanilla.id_peaje == id_peaje)
            for ventanilla_intance in ventanillas:
                print("Nro de ventanilla: ", ventanilla_intance.nro_ventanilla, " RFID: ", ventanilla_intance.tiene_rfid)
        except IntegrityError():
            print("Error: No se pudo consultar la ventanilla debido a una violación de restricción única.")


def eliminar_ventanilla(nombre, numero_eliminar):
    with psql_db.atomic():
        try:
            peaje_obj = peaje.get_or_none(peaje.nombre == nombre)
            peaje_id = peaje_obj.id_peaje
            if peaje_obj:
                ventanilla_obj = ventanilla.get_or_none(ventanilla.id_peaje == peaje_id, ventanilla.nro_ventanilla == numero_eliminar)
                if ventanilla_obj:
                    ventanilla_obj.delete_instance(recursive = False)
            psql_db.commit()
            print("Ventanilla eliminada correctamente.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo eliminar la ventanilla debido a una violación de restricción única.")