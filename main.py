from Config import *
from Tablas import *
        
def create_tables():
   psql_db.create_tables([peaje, propietario, persona, vehiculo, ventanilla, cuenta, empresa, propietario_tiene_vehiculo, persona_pariente, bonificacion, credito, debito, tipo_vehiculo, tarifa])


db_connect()
create_tables()
