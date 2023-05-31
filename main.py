from Config import *
from Tablas import *
from Personas import *
from Peaje import *
from Ventanilla import *
from Vehiculo import *
        
def create_tables():
   psql_db.create_tables([peaje,persona,propietario,propietario_tiene_vehiculo,vehiculo,ventanilla,empresa,tipo_vehiculo,tarifa,cuenta,persona_pariente,credito,bonificacion,debito,cuenta_propietario])


if __name__ == '__main__':
   db_connect()
   create_tables()
   estado = True
   while estado:
      opcion = int(input("\n1 Ingresar Datos \n2 Modifcar Datos \n3 Eliminar Datos \n4 Consultar Datos \n5 Salir \nOpcion: "))
      if opcion == 1:
         ingresar = int(input("\n1 Ingresar Persona \n2 Ingrsar Propietario \n3 Ingresar Cuenta \n4 Ingresar Vehiculo \n5 Ingresar Peaje \n6 Ingresar Ventanilla \nOpcion: "))
         if ingresar == 1:
            pass
         if ingresar == 2:
            pass
         if ingresar == 3:
            pass
         if ingresar == 4:
            matricula = int(input("Ingrese la matricula del vehiculo: "))
            tag_rfid = int(input("Ingrese el tag rfid del vehiculo: "))
            marca = input("Ingrese la marca del vehiculo: ")
            color = input("Ingrese el color del vehiculo: ")
            tipo = input("Ingrese el tipo de vehiculo: ")
            ingresar_vehiculo(matricula, tag_rfid, marca, color, tipo)
         if ingresar == 5:
            nombre_peaje= input("Ingrese el nombre del peaje: ")
            ruta = int(input("Ingrese la ruta en la que se encuentra el peaje: "))
            km = int(input("Ingrse el kilomnetro en el que se encuentra el peaje: "))
            telefono = input("Ingrese el telefono del peaje: ")
            ingresar_peaje(nombre_peaje, ruta, km, telefono)
         if ingresar == 6:
            nombre_p = input("Ingrese el nombre del peaje: ")
            numero_ventanilla = int(input("Ingrese el numero de la ventanilla: "))
            tiene_rfid = int(input("Ingrese 1 si la ventanilla tiene rfid o 0 si no lo tiene: "))
            ingresar_ventanilla(nombre_p, numero_ventanilla, tiene_rfid)
            
      if opcion == 5:
         estado = False

         
   # - Personas
   # - Propietarios
   # - Cuentas
   # - Vehículos
   # - Peajes
   # - Ventanillas