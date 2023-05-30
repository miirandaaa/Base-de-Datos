from main import *
from Tablas import *

def ingresar_peaje(nombre, ruta, km, telefono):
        if nombre is CharField(max_length=30) and ruta is SmallIntegerField() and km is SmallIntegerField() and telefono is IntegerField():
              peaje.create(nombre_peaje=nombre, ruta=ruta, km=km, telefono=telefono)