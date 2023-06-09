from Config import *
from Tablas import *
from Peaje import *
from Personas import *
from Ventanilla import *
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
            ingresar_propietario(dni, nombres, apellidos, celular, email, direccion, matricula, tag_rfid, marca, modelo, color, tipo)
            nuevo_prop = persona.get(persona.dni == dni)
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
            tiene_rfid = int(input("Ingrese 1 si la ventanilla tiene rfid o 0 si no lo tiene: "))
            ingresar_ventanilla(nombre_p, tiene_rfid)
      if opcion == 2:
         modificar = int(input("\n1 Modificar Persona \n2 Modificar Propietario \n3 Modificar Cuenta \n4 Modificar Vehiculo \n5 Modificar Peaje \n6 Modificar Ventanilla \nOpcion: "))
         if modificar == 1:
            mod = int(input("\n1 Modificar nombres \n2 Modificar apellidos \n3 Modificar celular \n4 Modificar email \n5 Modificar direccion \n6 Volver al menu \nOpcion: "))
            dni = int(input("Ingrese el dni de la persona que desea modificar: "))
            if mod == 1:
               nuevo_nombre = input("Ingrese el nuevo nombre: ")
               modificar_persona(dni, nuevo_nombre, 1)
            if mod == 2:
               nuevo_apellido = input("Ingrese el nuevo apellido: ")
               modificar_persona(dni, nuevo_apellido, 2)
            if mod == 3:
               nuevo_celular = int(input("Ingrese el nuevo celular: "))
               modificar_persona(dni, nuevo_celular, 3)
            if mod == 4:
               nuevo_email = input("Ingrese el nuevo email: ")
               modificar_persona(dni, nuevo_email, 4)
            if mod == 5:
               nueva_direccion = input("Ingrese la nueva direccion: ")
               modificar_persona(dni, nueva_direccion, 5)   
         if modificar == 2:
            pass
         if modificar == 3:
            pass
         if modificar == 4:
            mod = int(input("\n1 Modificar Tag RFID \n2 Modificar Marca \n3 Modificar Modelo \n4 Modificar Color \n5 Modificar Tipo \n6 Volver al menu \nOpcion: "))
            matricula = int(input("Ingrese la matricula del vehiculo que desea modificar: "))
            if mod == 1:
               nuevo_tag = int(input("Ingrese el nuevo tag rfid: "))
               modificar_vehiculo(matricula, nuevo_tag, 1)
            if mod == 2:
               nueva_marca = input("Ingrese la nueva marca: ")
               modificar_vehiculo(matricula, nueva_marca, 2)
            if mod == 3:
               nuevo_modelo = input("Ingrese el nuevo modelo: ")
               modificar_vehiculo(matricula, nuevo_modelo, 3)
            if mod == 4:
               nuevo_color = input("Ingrese el nuevo color: ")
               modificar_vehiculo(matricula, nuevo_color, 4)
            if mod == 5:
               nuevo_tipo = input("Ingrese el nuevo tipo: ")
               modificar_vehiculo(matricula, nuevo_tipo, 5)
         if modificar == 5:
            mod = int(input("\n1 Modificar Ruta \n2 Modificar Km \n3 Modificar Telefono \nOpcion: "))
            nombre = input("Ingrese el nombre del peaje que desea modificar: ")
            if mod == 1:
               nueva_ruta = int(input("Ingrese la nueva ruta: "))
               modificar_peaje(nombre, nueva_ruta, 1)
            if mod == 2:
               nuevo_km = int(input("Ingrese el nuevo km: "))
               modificar_peaje(nombre, nuevo_km, 2)
            if mod == 3:
               nuevo_telefono = input("Ingrese el nuevo telefono: ")
               modificar_peaje(nombre, nuevo_telefono, 3)
         if modificar == 6:
            pass
      if opcion == 3:
         eliminar = int(input("\n1 Eliminar Persona \n2 Eliminar Propietario \n3 Eliminar Cuenta \n4 Eliminar Vehiculo \n5 Eliminar Peaje \n6 Eliminar Ventanilla \nOpcion: "))
         pass
         if eliminar == 5: 
            nombre = input("Ingrese el nombre del peaje que desea eliminar: ")
            eliminar_peaje(nombre)
         if eliminar == 6:
            nro_ventanilla = int(input("Ingrese el numero de la ventanilla que desea eliminar: "))
            eliminar_ventanilla(nro_ventanilla)
      if opcion == 4:
         consultar = int(input("\n1 Consultar Persona \n2 Consultar Propietario \n3 Consultar Cuenta \n4 Consultar Vehiculo \n5 Consultar Peaje \n6 Consultar Ventanilla \nOpcion: "))
         if consultar == 1:
            persona_aconsultar = int(input("Ingrese el dni de la persona: "))
            consultar_persona(persona_aconsultar)
         if consultar == 2:
            id_prop = int(input("Ingrese el id del propietario: "))
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
            consultar_ventanilla(peaje_aconsultar)
      if opcion == 5:
         estado = False

  

   # - Modificar Persona
   # - Modificar Propietario
   # - Modificar Cuenta
   # - Modificar Ventanilla

   # - Eliminar Persona
   # - Eliminar Propietario
   # - Eliminar Cuenta
   # - Eliminar Vehículo
