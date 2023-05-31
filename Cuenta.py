from main import *
from Tablas import *
from Config import *
from Peaje import *
import datetime

def ingresar_cuenta (nro_cuenta, fecha_cuenta,id_prop):
    with psql_db.atomic():
        try:
            if cuenta.get_or_none(cuenta.nro_cuenta == nro_cuenta):
                print("La cuenta ingresada ya existe.")
            else:
                if propietario.get_or_none(propietario.id_propietario == id_prop):
                    data = fecha_cuenta.split("-")
                    date = datetime.date(int(data[0]),int(data[1]),int(data[2])) 
                    cuenta.create(nro_cuenta=nro_cuenta, fecha_creacion_cuenta=date, saldo = 0, id_propietario = id_prop)
                    psql_db.commit()
                    print("Cuenta creada correctamente.")
                else:
                    print("El propietario ingresado no existe.")
        except IntegrityError:
            psql_db.rollback()
            print("Error: No se pudo crear el peaje debido a una violación de restricción única.")

#CORROBORAR QUE FUNCIONE
def consultar_cuenta(cuenta_aconsultar):
    with psql_db.atomic():
        try:
            cuenta_querida = cuenta.get_by_id(cuenta_aconsultar)
            print(f"Nro Cuenta: {cuenta_querida.nro_cuenta}, Fecha Creacion: {cuenta_querida.fecha_creacion_cuenta}, Saldo: {cuenta_querida.saldo}, Id Propietario: {cuenta_querida.id_propietario}")
        except:
            print("Error: No se pudo consultar la cuenta debido a una violación de restricción única.")
    