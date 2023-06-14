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
                    ventanilla.create(id_peaje=peaje_obj.id_peaje, tiene_rfid=tiene_rfid)
                    psql_db.commit()
                    print("Ventanilla creada correctamente.")
                else: 
                    print("La ventanilla ya existe.")
            else:
                print("El peaje especificado no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo crear la ventanilla debido a una violación de restricción única.")

def modificar_ventanilla(peaje,numero,RFID):
    with psql_db.atomic():
        if peaje.get_or_none(nombre_peaje=peaje):
            peaje_querido=peaje.get_by_id(peaje)
            if ventanilla.get_or_none(nombre_peaje=peaje_querido,nro=numero):
                ventanilla_querida=ventanilla.get(nombre_peaje=peaje_querido,nro=numero)
                ventanilla_querida.tiene_rfid=RFID
                ventanilla_querida.save()
                psql_db.commit()
                print("Ventanilla modificada correctamente.")
            else:
                print("La ventanilla no existe.")
        else:
            print("El peaje no existe.")


        
    
    pass
    

def consultar_ventanilla(peaje_aconsultar):
    with psql_db.atomic():
        try:
            ventanilla_querida = ventanilla.get(nombre_peaje=peaje_aconsultar)
            ventanilla_querida.select()
        except IntegrityError():
            print("Error: No se pudo consultar la ventanilla debido a una violación de restricción única.")


def eliminar_ventanilla(numero_eliminar):
    with psql_db.atomic():
        try:
            ventanilla_eliminar = ventanilla.get_by_id(numero_eliminar)
            ventanilla_eliminar.delete_instance(recursive = False)
            psql_db.commit()
            print("Ventanilla eliminada correctamente.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo eliminar la ventanilla debido a una violación de restricción única.")