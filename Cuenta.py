from Tablas import *
from Config import *
from Peaje import *
import datetime

def ingresar_cuenta (nro_cuenta, fecha_cuenta, id):
    with psql_db.atomic():
        try:
            if cuenta.get_or_none(cuenta.nro_cuenta == nro_cuenta):
                print("La cuenta ingresada ya existe.")
            else:
                titular = propietario.get_or_none(propietario.id_propietario == id)
                if titular:
                    data = fecha_cuenta.split("-")
                    if int(data[1])<=12 and int(data[1])>0 and int(data[2])<=31 and int(data[2])>0:
                        date = datetime.date(int(data[0]),int(data[1]),int(data[2])) 
                        cuenta.create(nro_cuenta=nro_cuenta, fecha_creacion_cuenta=date, saldo = 0, id_propietario = titular.id_propietario)
                        psql_db.commit()
                        print("Cuenta creada correctamente.")
                    else:
                        print("La fecha ingresada no es valida.")
                else:
                    print("El propietario no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo crear el peaje debido a una violación de restricción única.")

def consultar_cuenta():
    with psql_db.atomic():
        try:
            cuenta_aconsultar = int(input("Ingrese el numero de cuenta: "))
            cuenta_querida = cuenta.get_by_id(cuenta_aconsultar)
            print(f"Nro Cuenta: {cuenta_querida.nro_cuenta}, Fecha Creacion: {cuenta_querida.fecha_creacion_cuenta}, Saldo: {cuenta_querida.saldo}, Id Propietario: {cuenta_querida.id_propietario}")
        except IntegrityError():
            print("Error: No se pudo consultar la cuenta debido a una violación de restricción única.")

def modificar_cuenta(num_cuenta, saldo):
    with psql_db.atomic():
        try:
            if cuenta.get_or_none(cuenta.nro_cuenta == num_cuenta):
                cuenta_a_modificar = cuenta.get_by_id(num_cuenta)
                cuenta_a_modificar.saldo = saldo
                cuenta_a_modificar.save()
                psql_db.commit()
                print("Cuenta modificada correctamente.")
            else:
                print("La cuenta no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo modificar la cuenta debido a una violación de restricción única.")

def eliminar_cuenta():
    with psql_db.atomic():
        try:
            num_cuenta = int(input("Ingrese el numero de cuenta que desea eliminar: "))
            if cuenta.get_or_none(cuenta.nro_cuenta == num_cuenta):
                cuenta_eliminar = cuenta.get_by_id(num_cuenta)
                cuenta_eliminar.delete_instance(recursive = True)
                psql_db.commit()
                print("Cuenta eliminada correctamente.")
            else:
                print("La cuenta no existe.")
        except IntegrityError():
            psql_db.rollback()
            print("Error: No se pudo eliminar la cuenta debido a una violación de restricción única.")
    