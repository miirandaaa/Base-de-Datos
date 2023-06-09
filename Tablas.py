from Config import *

class tipo_vehiculo (BaseModel):
   tipo = CharField(max_length=30, primary_key=True)

class tarifa (BaseModel):
   id_tarifa = AutoField(primary_key=True)
   tipo_vehiculo = ForeignKeyField(tipo_vehiculo)
   valor = DecimalField(max_digits=10, decimal_places=2)
   fecha_vigencia = DateField()

class peaje(BaseModel):
   id_peaje = AutoField(primary_key=True)
   nombre = CharField(max_length=30, unique=True)
   ruta = SmallIntegerField()
   km = SmallIntegerField()
   telefono_admin = CharField(max_length=30)

class propietario(BaseModel):
   id_propietario = AutoField(primary_key=True)
   tipo_propietario = CharField(max_length=30)

class cuenta(BaseModel):
   nro_cuenta = IntegerField(primary_key=True)
   fecha_creacion_cuenta = DateField()
   saldo = DecimalField(max_digits=10, decimal_places=2, default=0)
   id_propietario = ForeignKeyField(propietario)

class persona(BaseModel):
   dni = CharField(max_length=50, primary_key=True)
   id_propietario = ForeignKeyField(propietario)
   nombres = CharField(max_length=50)
   apellidos = CharField(max_length=50)
   celular = CharField(max_length=50)
   email = CharField(max_length=50)
   direccion = CharField(max_length=50)

class vehiculo(BaseModel):
   matricula = CharField(max_length = 20, primary_key=True)
   tag_rfid = CharField(max_length = 8, unique=True)
   marca = CharField(max_length = 30)
   modelo = CharField(max_length = 30)
   color = CharField(max_length = 20)
   tipo_vehiculo = ForeignKeyField(tipo_vehiculo)

class ventanilla(BaseModel):
   id_ventanilla = AutoField(primary_key = True)
   id_peaje = ForeignKeyField(peaje)
   nro_ventanilla = IntegerField()
   tiene_rfid = SmallIntegerField()


class empresa(BaseModel):
   id_propietario = ForeignKeyField(propietario)
   rut_empresa = CharField(max_length=12, primary_key=True)
   nombre_empresa = CharField(max_length=50)
   direccion_empresa = CharField(max_length=50)

class propietario_tiene_vehiculo(BaseModel):
    matricula = ForeignKeyField(vehiculo)
    id_propietario = ForeignKeyField(propietario)
    class Meta:
       primary_key = CompositeKey('matricula', 'id_propietario')

class persona_pariente(BaseModel):
   dni = ForeignKeyField(persona)
   dni_pariente = ForeignKeyField(persona)
   parentesco = CharField(max_length=30)
   class Meta:
      primary_key = CompositeKey('dni', 'dni_pariente')

class bonificacion(BaseModel):
   nro_cuenta = ForeignKeyField(cuenta)
   nombre_peaje = ForeignKeyField(peaje)
   fecha_otorgacion = DateField()
   fecha_renovacion = DateField()
   porcentaje = DecimalField(max_digits=5, decimal_places=2)
   motivo = CharField(max_length=100)
   class Meta:
      primary_key = CompositeKey('nro_cuenta', 'nombre_peaje', 'fecha_otorgacion')

class credito(BaseModel):
   nro_cuenta = ForeignKeyField(cuenta)
   fecha_hora_credito = DateTimeField()
   importe_credito = DecimalField(max_digits=10, decimal_places=2)
   class Meta:
      primary_key = CompositeKey('nro_cuenta', 'fecha_hora_credito')

class debito(BaseModel):
   matricula = ForeignKeyField(vehiculo)
   id_ventanilla = ForeignKeyField(ventanilla)
   fecha_hora_debito = DateTimeField()
   importe_debito = DecimalField(max_digits=10, decimal_places=2)
   class Meta:
      primary_key = CompositeKey('matricula', 'fecha_hora_debito')