from Config import *
from Tablas import *
from Peaje import *
from Personas import *
from Ventanilla import *
from Cuenta import *
from Personas import *
from Vehiculo import *
from Propietario import *
from Reportes import *
from main import *


def insertar_bonificacion():
    bonificacion = {
            "nro_cuenta": int(input("Ingrese el numero de cuenta: ")),
            "nombre_peaje": input("Ingrese el nombre del peaje: "),
            "porcentaje_descuento": int(input("Ingrese el porcentaje de descuento: ")),
            "motivo": input("Ingrese el motivo de la bonificacion: "),
            "fecha_otorgacion": input("Ingrese la fecha de otorgacion (YYYY-MM-DD): "),
            "fecha_renovacion": input("Ingrese la fecha de renovacion (YYYY-MM-DD): "),
            "comprobante_domicilio": input("Ingrese el comprobante de domicilio: "),	

   	      }
    bonificacion['_id'] = f"{bonificacion['nro_cuenta']}-{bonificacion['nombre_peaje']}-{bonificacion['fecha_otorgacion']}"
    cuenta_querida= cuenta.get_or_none(cuenta.nro_cuenta == bonificacion["nro_cuenta"])
    peaje_querido = peaje.get_or_none(peaje.nombre == bonificacion["nombre_peaje"])
            
    if cuenta_querida and peaje_querido:
        try:
            bonificaciones.insert_one(bonificacion)
            print("Bonificacion ingresada correctamente")
        except:
            print("Error al ingresar la bonificacion")
    else:           
        print("No existe la cuenta o el peaje")
    
    
    


def buscar_bonificacion():
    nro_cuenta= int(input("Ingrese el numero de cuenta: "))
    nombre_peaje = input("Ingrese el nombre del peaje: ")
    fecha_otorgacion = input("Ingrese la fecha de otorgacion: ")
    cuenta_q = cuenta.get_or_none(cuenta.nro_cuenta == nro_cuenta)
    peaje_q = peaje.get_or_none(peaje.nombre == nombre_peaje)
    if cuenta_q and peaje_q:
        try:
            bonificacion = bonificaciones.find_one({"nro_cuenta": nro_cuenta, "nombre_peaje": nombre_peaje, "fecha_otorgacion": fecha_otorgacion})
            print(bonificacion)
        except:
            print("La bonificacion no existe.")
    else:
        print("La cuenta o el peaje no existe.")
