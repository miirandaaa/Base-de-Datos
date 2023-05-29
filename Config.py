from sshtunnel import SSHTunnelForwarder
from configparser import ConfigParser
from peewee import *
#from pymongo import *

appcfg = ConfigParser ()
appcfg.read ('App.cfg')

#mappcfg = ConfigParser ()
#mappcfg.read ('App2.cfg')

server = SSHTunnelForwarder (
               ssh_address_or_host = appcfg.get ('ssh_tunnel','ssh_host'),
               ssh_port = appcfg.getint('ssh_tunnel', 'ssh_port'),
               ssh_username = appcfg.get ('ssh_tunnel', 'ssh_username'),
               ssh_password = appcfg.get ('ssh_tunnel', 'ssh_password'),
               remote_bind_address = (appcfg.get ('ssh_tunnel', 'remote_address'), appcfg.getint ('ssh_tunnel', 'remote_port')),
               local_bind_address = (appcfg.get ('ssh_tunnel', 'local_address'), appcfg.getint ('ssh_tunnel', 'local_port'))
              )

psql_db = PostgresqlDatabase (
               appcfg.get ('database', 'db_name'), 
               host = appcfg.get ('database', 'db_host'),
               port = appcfg.getint ('database', 'db_port'),
               user = appcfg.get ('database', 'db_user'),
               password = appcfg.get ('database', 'db_pass')
              )

#mserver = SSHTunnelForwarder (
#               ssh_address_or_host = mappcfg.get ('ssh_tunnel','ssh_host'),
#               ssh_port = mappcfg.getint('ssh_tunnel', 'ssh_port'),
#               ssh_username = mappcfg.get ('ssh_tunnel', 'ssh_username'),
#               ssh_password = mappcfg.get ('ssh_tunnel', 'ssh_password'),
#               remote_bind_address = (mappcfg.get ('ssh_tunnel', 'remote_address'), mappcfg.getint ('ssh_tunnel', 'remote_port')),
#               local_bind_address = (mappcfg.get ('ssh_tunnel', 'local_address'), mappcfg.getint ('ssh_tunnel', 'local_port'))
#              )

#mongo_db = MongoClient ("mongodb://localhost:27017")
#my_mongo_db = mongo_db.mdbg3.Bonificaciones

def db_connect ():
  if appcfg.getboolean ('global', 'use_ssh_tunnel'):
    print ('INFO: Opening ssh tunnel ...')
    server.start()
    if not server.is_active:
      print ('ERROR: Cannot established ssh tunnel!')
      return (False)
    
  print ('INFO: Connecting to database ...')
  psql_db.connect()
  return (True)


class BaseModel (Model):

    class Meta:
        database = psql_db

class tarifa (BaseModel):
   id_tarifa = IntegerField()
   tipo_vehiculo = CharField(max_length=30)
   valor = DecimalField(max_digits=10, decimal_places=2)
   fecha_vigencia = DateField()

   class Meta:
      primary_key = CompositeKey('id_tarifa', 'fecha_vigencia')

def create_tables():
   psql_db.create_tables([tarifa])

"""
CREATE TABLE tarifa (
   id_tarifa INT NOT NULL,
   tipo_vehiculo VARCHAR(30) NOT NULL,
   valor DECIMAL(10, 2) NOT NULL,
   fecha_vigencia DATE NOT NULL,
   CONSTRAINT pk_tarifa PRIMARY KEY (id_tarifa, fecha_vigencia)
);

CREATE TABLE tipo_vehiculo (
   tipo VARCHAR(30) NOT NULL,
   CONSTRAINT pk_tipo_vehiculo PRIMARY KEY (tipo)
);

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

CREATE TABLE peaje (
   nombre VARCHAR(30) NOT NULL,
   ruta SMALLINT NOT NULL,
   km SMALLINT NOT NULL,
   telefono_admin INT NOT NULL,
   CONSTRAINT pk_peaje PRIMARY KEY (nombre),
   CONSTRAINT uk_peake UNIQUE (ruta, km)
);

CREATE TABLE ventanilla (
   nombre_peaje VARCHAR(30) NOT NULL,
   nro SMALLINT NOT NULL,
   tiene_rfid BOOLEAN NOT NULL,
   CONSTRAINT pk_ventanilla PRIMARY KEY (nombre_peaje, nro),
   CONSTRAINT fk1_ventanilla FOREIGN KEY (nombre_peaje) REFERENCES peaje(nombre)
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
CREATE TABLE propietario_tiene_vehiculo (
   id_propietario INT NOT NULL,
   matricula CHAR(6) NOT NULL,
   CONSTRAINT pk_prop_tiene_veh PRIMARY KEY (id_propietario, matricula),
   CONSTRAINT fk1_prop_tiene_veh FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario),
   CONSTRAINT fk2_prop_tiene_veh FOREIGN KEY (matricula) REFERENCES vehiculo(matricula)
);
CREATE TABLE vehiculo (
   matricula CHAR(6) NOT NULL,
   tag_rfid CHAR(8) NOT NULL,
   tipo_vehiculo VARCHAR(30) NOT NULL,
   marca VARCHAR(30) NOT NULL,
   modelo VARCHAR(30) NOT NULL,
   color VARCHAR(20) NOT NULL,
   CONSTRAINT pk_vehiculo PRIMARY KEY (matricula),
   CONSTRAINT uk_vehiculo UNIQUE (tag_rfid),
   CONSTRAINT fk1_vehiculo FOREIGN KEY (tipo_vehiculo) REFERENCES tipo_vehiculo(tipo)
);
CREATE TABLE persona (
   dni VARCHAR(50) NOT NULL,
   id_propietario INT NOT NULL,
   nombres VARCHAR(50) NOT NULL,
   apellidos VARCHAR(50) NOT NULL,
   celular VARCHAR(50) NOT NULL,
   email VARCHAR(50) NOT NULL,
   direccion VARCHAR(50) NOT NULL,
   CONSTRAINT pk_persona PRIMARY KEY (dni),
   CONSTRAINT fk1_persona FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario)
);
CREATE TABLE propietario (
   id_propietario INT NOT NULL,
   tipo_propietario VARCHAR(30) NOT NULL,
   CONSTRAINT pk_propietario PRIMARY KEY (id_propietario)
  );
CREATE TABLE empresa (
   id_propietario INT NOT NULL,
   rut_empresa CHAR(12) NOT NULL,
   nombre_empresa VARCHAR(50) NOT NULL,
   direccion_empresa VARCHAR(50) NOT NULL,
   CONSTRAINT pk_empresa PRIMARY KEY (rut_empresa),
   CONSTRAINT fk1_empresa FOREIGN KEY (id_propietario) REFERENCES propietario(id_propietario)
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

