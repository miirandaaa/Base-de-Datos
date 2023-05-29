from Config import *

class tarifa (BaseModel):
   id_tarifa = IntegerField()
   tipo_vehiculo = CharField(max_length=30)
   valor = DecimalField(max_digits=10, decimal_places=2)
   fecha_vigencia = DateField()

   class Meta:
      primary_key = CompositeKey('id_tarifa', 'fecha_vigencia')

class tipo_vehiculo (BaseModel):
   tipo = CharField(max_length=30, primary_key=True)


def create_tables():
   psql_db.create_tables([tarifa, tipo_vehiculo])

db_connect()
create_tables()