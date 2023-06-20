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
from Credito import *
from Bonificacion import *
from Debito import *
db_conn['rdbms'] = db_conn['rdbms']
        
def create_tables():
   db_conn['rdbms'].create_tables([peaje,persona,propietario,propietario_tiene_vehiculo,vehiculo,ventanilla,empresa,tipo_vehiculo,tarifa,cuenta,persona_pariente,credito,bonificacion,])

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
   id_bonificacion = f"{nro_cuenta}-{nombre_peaje}-{fecha_otorgacion}"
   bonificacion = bonificaciones.find_one({"_id": id_bonificacion})
   if bonificacion:
        print("Bonificacion encontrada")
        print(bonificacion)
   else:
         print("Bonificacion no encontrada")
    
  

if __name__ == '__main__':
   db_connect()
   create_tables()
   db = db_conn['nosql']['dbd2g04']
   bonificaciones = db['bonificaciones']
   #tipo_vehiculo.create(tipo ='auto') and tipo_vehiculo.create(tipo ='camioneta') and tipo_vehiculo.create(tipo ='camion') and tipo_vehiculo.create(tipo='Bus') and tipo_vehiculo.create(tipo='Moto')
   estado = True
   while estado:
      opcion = int(input("\n1 Ingresar Datos \n2 Modifcar Datos \n3 Eliminar Datos \n4 Consultar Datos \n5 Reportes \n6 Registar credito o debito \n7 Salir \nOpcion: "))
      if opcion == 1:
         ingresar = int(input("\n1 Ingresar Propietario \n2 Ingresar Cuenta \n3 Ingresar Vehiculo \n4 Ingresar Peaje \n5 Ingresar Ventanilla \n6 Ingresar Bonificacion \nOpcion: "))
         if ingresar == 1:
            dni = int(input("Ingrese el dni del propietario: "))
            nombres = input("Ingrese los nombres del propietario: ")
            apellidos = input("Ingrese los apellidos del propietario: ")
            celular = int(input("Ingrese el celular del propietario: "))
            email = input("Ingrese el email del propietario: ")
            direccion = input("Ingrese la direccion del propietario: ")
            matricula = int(input("Ingrese la matricula del vehiculo: "))
            ingresar_propietario(dni, nombres, apellidos, celular, email, direccion, matricula)
            asociar=int(input("Desea asociar su vehiculo a una cuenta de un pariente? \n1 Si \n2 No \nOpcion: "))
            if asociar==1:
               dni_pariente=int(input("Ingrese el dni del pariente: "))
               tipo=input("Ingrese el tipo de parentesco:  ")
               asociar_pariente(dni,dni_pariente,tipo)
            if asociar==2:
               print("No se asociara el vehiculo a una cuenta de un pariente")


            db_conn['rdbms'].commit()
         if ingresar == 2:
            nro_cuenta = int(input("Ingrese el numero de cuenta: "))
            fecha_cuenta = input("Ingrese la fecha de creacion de la cuenta (YYYY-MM-DD): ")
            dni = int(input("Ingrese el dni del propietario: "))
            ingresar_cuenta(nro_cuenta, fecha_cuenta, dni)
         if ingresar == 3:
            dni_prop = int(input("Ingrese el dni del propietario: "))
            matricula = int(input("Ingrese la matricula del vehiculo: "))
            tag_rfid = int(input("Ingrese el tag rfid del vehiculo: "))
            marca = input("Ingrese la marca del vehiculo: ")
            modelo = input("Ingrese el modelo del vehiculo: ")
            color = input("Ingrese el color del vehiculo: ")
            tipo = input("Ingrese el tipo de vehiculo: ")
            ingresar_vehiculo(dni_prop,matricula, tag_rfid, marca, modelo, color, tipo)
         if ingresar == 4:
            nombre_peaje= input("Ingrese el nombre del peaje: ")
            ruta = int(input("Ingrese la ruta en la que se encuentra el peaje: "))
            km = int(input("Ingrse el kilomnetro en el que se encuentra el peaje: "))
            telefono = input("Ingrese el telefono del peaje: ")
            ingresar_peaje(nombre_peaje, ruta, km, telefono)
         if ingresar == 5:
            nombre_p = input("Ingrese el nombre del peaje: ")
            nro_ventanilla = int(input("Ingrese el numero de la ventanilla: "))
            tiene_rfid = int(input("Ingrese 1 si la ventanilla tiene rfid o 0 si no lo tiene: "))
            ingresar_ventanilla(nombre_p, nro_ventanilla, tiene_rfid)
         if ingresar == 6:
            insertar_bonificacion()
            

      if opcion == 2:
         modificar = int(input("\n1 Modificar Persona \n2 Modificar Cuenta \n3 Modificar Vehiculo \n4 Modificar Peaje \n5 Modificar Ventanilla  \nOpcion: "))
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
            nro_cuenta = int(input("Ingrese el numero de cuenta que desea modificar su saldo: "))
            saldo = int(input("Ingrese el nuevo saldo: "))
            modificar_cuenta(nro_cuenta, saldo)
         if modificar == 3:
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
         if modificar == 4:
            mod = int(input("\n1 Modificar Ruta \n2 Modificar Km \n3 Modificar Telefono \n4 Modificar Nombre\nOpcion: "))
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
            if mod == 4:
               nuevo_nombre = input("Ingrese el nuevo nombre: ")
               modificar_peaje(nombre, nuevo_nombre, 4)
         if modificar == 5:
            peaje_querido = input("Ingrese el nombre del peaje al que pertenece la ventanilla que desea modificar: ")
            nro_ventanilla = int(input("Ingrese el numero de la ventanilla que desea modificar: "))
            mod = int(input("Ingrese ""1"" si la ventanilla tiene rfid o ""0"" si no lo tiene: "))
            modificar_ventanilla(peaje_querido, nro_ventanilla, mod)
      if opcion == 3:
         eliminar = int(input("\n1 Eliminar Persona \n2 Eliminar Cuenta \n3 Eliminar Vehiculo \n4 Eliminar Peaje \n5 Eliminar Ventanilla  \nOpcion: "))
         pass
         if eliminar == 1:
            eliminar_persona()
         if eliminar == 2:
            eliminar_cuenta()
         if eliminar == 3:
            eliminar_vehiculo()
         if eliminar == 4: 
            eliminar_peaje()
         if eliminar == 5:
            peaje_querido = input("Ingrese el nombre del peaje al que pertenece la ventanilla que desea eliminar: ")
            nro_ventanilla = int(input("Ingrese el numero de la ventanilla que desea eliminar: "))
            eliminar_ventanilla(peaje_querido, nro_ventanilla)
      if opcion == 4:
         consultar = int(input("\n1 Consultar Persona \n2 Consultar Propietario \n3 Consultar Cuenta \n4 Consultar Vehiculo \n5 Consultar Peaje \n6 Consultar Ventanilla \n7 Consultar Bonificacion \nOpcion: "))
         if consultar == 1:
            consultar_persona()
         if consultar == 2:
            consultar_propietario()
         if consultar == 3:
            consultar_cuenta()
         if consultar == 4:
            consultar_vehiculo()
         if consultar == 5:
            consultar_peaje()
         if consultar == 6:
            consultar_ventanilla()
         if consultar == 7:
            buscar_bonificacion()
      if opcion == 5:
         reporte = int(input("\n1 Listado de Propietario y sus Vehiculos \n2 Listado de Cuentas con su Titular y sus Vehiculos asociados \nOpcion:"))
         if reporte == 1:
            reporte_titular_y_vehiculos()
         if reporte == 2:
            listado_cuenta_con_titular_y_vehiculos()
      if opcion == 6:
         registro = int(input("\n1 Acreditar saldo \n2 Registrar pasada (debito) \nOpcion:"))
         if registro == 1:
            acreditacion()   
         if registro == 2:
            debito()
      if opcion == 7:
         estado = False
