from Config import *
from Tablas import *
from Peaje import *
from Personas import *
from Ventanilla import *
from datetime import date
from Cuenta import *
from Personas import *
from Vehiculo import *
from Propietario import *
        
def create_tables():
   psql_db.create_tables([peaje,persona,propietario,propietario_tiene_vehiculo,vehiculo,ventanilla,empresa,tipo_vehiculo,tarifa,cuenta,persona_pariente,credito,bonificacion,debito,])


if __name__ == '__main__':
   db_connect()
   create_tables()
   estado = True
   while estado:
      opcion = int(input("\n1 Ingresar Datos \n2 Modifcar Datos \n3 Eliminar Datos \n4 Consultar Datos \n5 Salir \nOpcion: "))
      if opcion == 1:
         ingresar = int(input("\n1 Ingrsar Propietario \n2 Ingresar Cuenta \n3 Ingresar Vehiculo \n4 Ingresar Peaje \n5 Ingresar Ventanilla \nOpcion: "))
         if ingresar == 1:
            dni = int(input("Ingrese el dni del propietario: "))
            nombres = input("Ingrese los nombres del propietario: ")
            apellidos = input("Ingrese los apellidos del propietario: ")
            celular = int(input("Ingrese el celular del propietario: "))
            email = input("Ingrese el email del propietario: ")
            direccion = input("Ingrese la direccion del propietario: ")
            matricula = int(input("Ingrese la matricula del vehiculo: "))
            tag_rfid = int(input("Ingrese el tag rfid del vehiculo: "))
            marca = input("Ingrese la marca del vehiculo: ")
            modelo = input("Ingrese el modelo del vehiculo: ")
            color = input("Ingrese el color del vehiculo: ")
            tipo = input("Ingrese el tipo de vehiculo: ")
            nuevo_prop = ingresar_propietario(dni, nombres, apellidos, celular, email, direccion, matricula, tag_rfid, marca, modelo, color, tipo)
            propietario_tiene_vehiculo.create(id_propietario=nuevo_prop.id_propietario, matricula=matricula)
            psql_db.commit()
         if ingresar == 2:
            nro_cuenta = int(input("Ingrese el numero de cuenta: "))
            fecha_cuenta = input("Ingrese la fecha de creacion de la cuenta (YYYY-MM-DD): ")
            id_prop = int(input("Ingrese el id del propietario: "))
            ingresar_cuenta(nro_cuenta, fecha_cuenta, id_prop)
         if ingresar == 3:
            matricula = int(input("Ingrese la matricula del vehiculo: "))
            tag_rfid = int(input("Ingrese el tag rfid del vehiculo: "))
            marca = input("Ingrese la marca del vehiculo: ")
            modelo = input("Ingrese el modelo del vehiculo: ")
            color = input("Ingrese el color del vehiculo: ")
            tipo = input("Ingrese el tipo de vehiculo: ")
            ingresar_vehiculo(matricula, tag_rfid, marca, modelo, color, tipo)
         if ingresar == 4:
            nombre_peaje= input("Ingrese el nombre del peaje: ")
            ruta = int(input("Ingrese la ruta en la que se encuentra el peaje: "))
            km = int(input("Ingrse el kilomnetro en el que se encuentra el peaje: "))
            telefono = input("Ingrese el telefono del peaje: ")
            ingresar_peaje(nombre_peaje, ruta, km, telefono)
         if ingresar == 5:
            nombre_p = input("Ingrese el nombre del peaje: ")
            numero_ventanilla = int(input("Ingrese el numero de la ventanilla: "))
            tiene_rfid = int(input("Ingrese 1 si la ventanilla tiene rfid o 0 si no lo tiene: "))
            ingresar_ventanilla(nombre_p, numero_ventanilla, tiene_rfid)
      if opcion == 2:
         modificar = input("\n1 Modificar Persona \n2 Modificar Propietario \n3 Modificar Cuenta \n4 Modificar Vehiculo \n5 Modificar Peaje \n6 Modificar Ventanilla \nOpcion: ")
         if modificar == 1:
            pass
         if modificar == 2:
            pass
         if modificar == 3:
            pass
         if modificar == 4:
            pass
         if modificar == 5:
            nombre = input("Ingrese el nombre del peaje a modificar: ")
            ruta = int(input("Ingrese la ruta en la que se encuentra el peaje: "))
            km = int(input("Ingrse el kilomnetro en el que se encuentra el peaje: "))
            telefono = input("Ingrese el telefono del peaje: ")
            modificar_peaje(nombre, ruta, km, telefono)
         if modificar == 6:
            pass
      if opcion == 3:
         pass
      if opcion == 4:
         consultar = int(input("\n1 Consultar Persona \n2 Consultar Propietario \n3 Consultar Cuenta \n4 Consultar Vehiculo \n5 Consultar Peaje \n6 Consultar Ventanilla \nOpcion: "))
         if consultar == 1:
            persona_aconsultar = int(input("Ingrese el dni de la persona: "))
            consultar_persona(persona_aconsultar)
         if consultar == 2:
            consultar_propietario(id_prop)
         if consultar == 3:
            cuenta_aconsultar = int(input("Ingrese el numero de cuenta: "))
            consultar_cuenta(cuenta_aconsultar)
         if consultar == 4:
            vehiculo_aconsultar = int(input("Ingrese la matricula del vehiculo: "))
            consultar_vehiuclo(vehiculo_aconsultar)
         if consultar == 5:
            peaje_aconsultar = input("Ingrese el nombre del peaje: ")
            consultar_peaje(peaje_aconsultar)
         if consultar == 6:
            peaje_aconsultar = input("Ingrese el nombre del peaje: ")
            ventanilla_aconsultar = int(input("Ingrese el numero de la ventanilla: "))
            consultar_ventanilla(peaje_aconsultar, ventanilla_aconsultar)
      if opcion == 5:
         estado = False

   # - Consultar Propietario

   # - Modificar Persona
   # - Modificar Propietario
   # - Modificar Cuenta
   # - Modificar Vehículo
   # - Modificar Ventanilla

   # - Eliminar Persona
   # - Eliminar Propietario
   # - Eliminar Cuenta
   # - Eliminar Vehículo
   # - Eliminar Peaje
   # - Eliminar Ventanilla
