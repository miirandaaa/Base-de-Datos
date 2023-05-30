from Config import *
from Tablas import *
        
def create_tables():
   psql_db.create_tables([peaje,persona,propietario,propietario_tiene_vehiculo,vehiculo,ventanilla,empresa,tipo_vehiculo,tarifa,cuenta,persona_pariente,credito,bonificacion,debito,cuenta_propietario])

# db_connect()
# create_tables()

if __name__ == '__main__':
   estado = True
   while estado:
      opcion = int(input("\n1 Ingresar Datos \n2 Modifcar Datos \n3 Eliminar Datos \n4 Consultar Datos \n5 Salir \nOpcion: "))
      if opcion == 1:
         ingresar = int(input("\n1 Ingresar Persona \n2 Ingrsar Propietario \n3 Ingresar Cuenta \n4 Ingresar Vehiculo \n5 Ingresar Peaje \n6 Ingresar Ventanilla \nOpcion: "))
      if opcion == 5:
         estado = False

      
# - Personas
# - Propietarios
# - Cuentas
# - Vehículos
# - Peajes
# - Ventanillas