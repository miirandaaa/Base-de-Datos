from Tablas import *
from Config import *
from peewee import *
db_conn['rdbms'] = db_conn['rdbms']
def ingresar_peaje(nombre_peaje, ruta, km, telefono): #Preguntar si se tiene que crear con ventanillas o no
     with db_conn['rdbms'].atomic():
        try:
            if peaje.get_or_none(peaje.nombre == nombre_peaje):
                print("El peaje ingresado ya existe.")
            else:
                peaje.create(nombre=nombre_peaje, ruta=ruta, km=km, telefono_admin=telefono)
                db_conn['rdbms'].commit()
                print("Peaje creado correctamente.")
        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo crear el peaje debido a una violación de restricción única.")

def consultar_peaje():
    with db_conn['rdbms'].atomic():
        try:
            peaje_aconsultar = input("Ingrese el nombre del peaje: ")
            peaje_querido = peaje.get(peaje.nombre == peaje_aconsultar)
            print(f"ID Peaje: {peaje_querido.id_peaje} \nNombre: {peaje_querido.nombre} \nRuta: {peaje_querido.ruta} \nKm: {peaje_querido.km} \nTelefono: {peaje_querido.telefono_admin}")
        except IntegrityError():
            print("Error: No se pudo consultar el peaje debido a una violación de restricción única.")

def modificar_peaje(key, modifcar, opcion): 
    with db_conn['rdbms'].atomic():
        try:
            if peaje.get_or_none(peaje.nombre == key):
                p_mod = peaje.get(peaje.nombre == key)
                if opcion == 1:
                    p_mod.ruta = modifcar
                if opcion == 2:
                    p_mod.km = modifcar
                if opcion == 3:
                    p_mod.telefono_admin = modifcar
                if opcion == 4:
                    p_mod.nombre = modifcar
                p_mod.save()
                db_conn['rdbms'].commit()
            else:
                print("El peaje ingresado no existe.")
        except:
            db_conn['rdbms'].rollback()
            print("Error: No se pudo modificar el peaje debido a una violación de restricción única.")

def eliminar_peaje():
    with db_conn['rdbms'].atomic():
        try:
            nombre = input("Ingrese el nombre del peaje que desea eliminar: ")
            peaje_eliminar = peaje.get(peaje.nombre == nombre)
            peaje_eliminar.delete_instance(recursive = True)
            db_conn['rdbms'].commit()
            print("Peaje eliminado correctamente.")
        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo eliminar el peaje debido a una violación de restricción única.")
