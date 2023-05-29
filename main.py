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

class peaje(BaseModel):
   nombre = CharField(max_length=30, primary_key=True)
   ruta = SmallIntegerField()
   km = SmallIntegerField()
   telefono_admin = IntegerField()
   #falta setear ruta,km como unique ambas en conjunto CONSTRAINT uk_peake UNIQUE (ruta, km);

class propietario(BaseModel):
   id_propietario = IntegerField(primary_key=True)
   tipo_propietario = CharField (max_length=30)

class persona (BaseModel):
   dni = CharField(max_length=50, primary_key=True)
   id_propietario = ForeignKeyField(propietario)
   nombres = CharField(max_length=50)
   apellidos = CharField(max_length=50)
   celular = CharField(max_length=50)
   email = CharField(max_length=50)
   direccion = CharField(max_length=50)

class vehiculo(BaseModel):
   matricula = CharField(max_length = 6, primary_key=True)
   tag_rfid = CharField(max_length = 8, unique=True)
   marca = CharField(max_length = 30)
   color = CharField(max_length = 20)
   tipo_vehiculo = ForeignKeyField(tipo_vehiculo)

class ventanilla(BaseModel):
   nombre_peaje = ForeignKeyField(peaje)
   nro = SmallIntegerField()
   tiene_rfid = BooleanField()

   class Meta:
      primary_key = CompositeKey('nombre_peaje', 'nro')

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
        
def create_tables():
   psql_db.create_tables([tarifa, tipo_vehiculo, peaje, propietario, persona, empresa, vehiculo, propietario_tiene_vehiculo,ventanilla])


db_connect()
create_tables()


"""
CREATE TABLE bonificacion (
   nro_cuenta INT NOT NULL,
   nombre_peaje VARCHAR(30) NOT NULL,
   fecha_otorgacion DATE NOT NULL,
   fecha_renovacion DATE NOT NULL,
   porcentaje DECIMAL(5, 2) NOT NULL,
   motivo VARCHAR(100) NOT NULL,
   CONSTRAINT pk_bonificacion PRIMARY KEY (nro_cuenta, nombre_peaje, fecha_otorgacion),
   CONSTRAINT fk1_bonificacion  FOREIGN KEY (nro_cuenta) REFERENCES cuenta(nro_cuenta),
   CONSTRAINT fk2_bonificacion  FOREIGN KEY (nombre_peaje) REFERENCES peaje(nombre)
);

CREATE TABLE debito (
   matricula CHAR(6) NOT NULL,
   nombre_peaje VARCHAR(30) NOT NULL,
   nro_ventanilla SMALLINT NOT NULL,
   fecha_hora_debito TIMESTAMP NOT NULL,
   importe_debito DECIMAL(10, 2) NOT NULL,
   CONSTRAINT pk_debito PRIMARY KEY (matricula, fecha_hora_debito),
   CONSTRAINT fk1_debito FOREIGN KEY (matricula) REFERENCES vehiculo(matricula),
   CONSTRAINT fk2_debito FOREIGN KEY (nombre_peaje, nro_ventanilla) REFERENCES ventanilla(nombre_peaje, nro)
);


CREATE TABLE cuenta (
   id_propietario INT NOT NULL,
   nro_cuenta INT NOT NULL,
   fecha_creacion_cuenta DATE NOT NULL,
   saldo DECIMAL(10, 2) DEFAULT 0,
   CONSTRAINT pk_cuenta PRIMARY KEY (nro_cuenta),
   CONSTRAINT fk1_cuenta FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario)
);
CREATE TABLE credito (
   nro_cuenta INT NOT NULL,
   fecha_hora_credito TIMESTAMP NOT NULL,
   importe_credito DECIMAL(10, 2) NOT NULL,
   CONSTRAINT pk_credito PRIMARY KEY (nro_cuenta, fecha_hora_credito),
   CONSTRAINT fk1_credito FOREIGN KEY (nro_cuenta) REFERENCES cuenta(nro_cuenta)
);
CREATE TABLE persona_pariente (
   dni VARCHAR(50) NOT NULL,
   dni_pariente VARCHAR(50) NOT NULL,
   parentesco VARCHAR(30) NOT NULL,
   CONSTRAINT pk_persona_pariente PRIMARY KEY (dni, dni_pariente),
   CONSTRAINT fk1_persona_pariente FOREIGN KEY (dni) REFERENCES persona(dni),
   CONSTRAINT fk2_persona_pariente FOREIGN KEY (dni_pariente) REFERENCES persona(dni));
"""
