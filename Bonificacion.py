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

def insertar_bonificacion(bonificacion):
   
    db_connect()
    db = db_conn['nosql']['dbd2g04']
    bonificaciones = db['bonificaciones']

   
    bonificaciones.insert_one(bonificacion)

# Ejemplo de uso
bonificacion = {
    "nro_cuenta": 123,
    "nombre_peaje": "Peaje A",
    "porcentaje_descuento": 10,
    "motivo": "Cliente frecuente",
    "fecha_otorgacion": "2023-06-19",
    "fecha_renovacion": "2024-06-19",
    "comprobante_domicilio": "www.comprobante.com",

}

try:
    insertar_bonificacion(bonificacion)
    print("Bonificación insertada correctamente")
except Exception as e:
    print(e)