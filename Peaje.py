from main import *
from Tablas import *

def ingresar_peaje(nombre_peaje, ruta, km, telefono):
        if isinstance(nombre_peaje,str) and isinstance(ruta,int) and isinstance(km,int) and isinstance(telefono,int):
              peaje.create(nombre_peaje=nombre_peaje, ruta=ruta, km=km, telefono=telefono)