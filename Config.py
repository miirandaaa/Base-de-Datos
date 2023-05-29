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
