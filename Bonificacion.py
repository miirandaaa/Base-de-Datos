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



