from main import *
from Tablas import *
from Config import *
from Peaje import *

def ingresar_cuenta (nro_cuenta, fecha_cuenta,id_prop):
    with psql_db.atomic():
        try:
            if cuenta.get_or_none(cuenta.nro_cuenta == nro_cuenta):
                print("La cuenta ingresada ya existe.")
            else:
                if propietario.get_or_none(propietario.id_propietario == id_prop):
                    cuenta.create(nro_cuenta=nro_cuenta, fecha_creacion_cuenta = fecha_cuenta, saldo = 0, id_propietario = id_prop)
                    print("Cuenta creada correctamente.")
                else:
                    print("El propietario ingresado no existe.")
        except IntegrityError:
            print("Error: No se pudo crear el peaje debido a una violación de restricción única.")

    