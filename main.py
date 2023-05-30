from Config import *
from Tablas import *
        
def create_tables():
   psql_db.create_tables([peaje,persona,propietario,propietario_tiene_vehiculo,vehiculo,ventanilla,empresa,tipo_vehiculo,tarifa,cuenta,persona_pariente,credito,bonificacion,debito,cuenta_propietario])

db_connect()
create_tables()

if __name__ == '__main__':
   opcion = print ("Ingrese una opcion: nl\ Ingresar ")