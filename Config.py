"""
Config.py

Author : Diego Lopez Roig
Created: 29/10/2022
Version: 1.0
Purpose: Define the class from which to extend other classes that will manipulate database data using the peewee ORM.
         Define the functions to connect to a PostgreSQL database using or not an SSH tunnel.
         
History of changes:
Date       Author               Description
---------- -------------------- -------------------------------------------------------------------------
11/06/2023 Diego Lopez Roig     Exception checks added
                                New checks to validate that certain sections exist in configuration file
                                New functions read_app_cfg() and open_ssh_tunnel(), db_pg_conn() and db_mongo_conn()
                                Invoked function now depend on database section name
"""
import time
from pathlib import Path
from sshtunnel import SSHTunnelForwarder
from configparser import ConfigParser
from peewee import *
from pymongo import MongoClient

# ---------------------------------------------------------------------------
# Global constants
# ---------------------------------------------------------------------------
APP_CFG_FILE = 'App.cfg'
CONFIG_SECTION_NAMES = {
  'mandatory' : {
    'rdbms' : 'postgresql',
    'nosql' : 'mongodb'
  },
  'ssh_tunnel' : {
    'rdbms' : 'pg_ssh_tunnel',
    'nosql' : 'mongo_ssh_tunnel'    
  }
}

# ---------------------------------------------------------------------------
# Global variables
# ---------------------------------------------------------------------------
db_conn = {'rdbms' : PostgresqlDatabase(None)} # Database handlers for rdbms and nosql
ssh_tunnel = {}                                   # SSH tunnel handlers to connect to databases

# ---------------------------------------------------------------------------
# Class to use as base class for peewee model classes
# ---------------------------------------------------------------------------
class BaseModel (Model):
    class Meta:
        database = db_conn['rdbms']
        
# ---------------------------------------------------------------------------
# read_app_cfg ()
# ---------------------------------------------------------------------------
def read_app_cfg ():
  try:
    app_cfg = ConfigParser ()
    cfg_file_name = None
    for k in Path('.').rglob (APP_CFG_FILE):
      cfg_file_name = k
    
    if not cfg_file_name:
      raise Exception ('ERROR: Cloud not find configuration file {} !'.format (APP_CFG_FILE))

    files  = app_cfg.read (cfg_file_name)
    if not files:
      raise Exception ('ERROR: Could not read configuration file {} !'.format (cfg_file_name))
  
    return (app_cfg)
  
  except:
    raise
  
# ---------------------------------------------------------------------------
# open_ssh_tunnel ()
# ---------------------------------------------------------------------------
def open_ssh_tunnel (ssh_cfg):
  try:
    server = SSHTunnelForwarder (
               ssh_address_or_host = ssh_cfg['ssh_host'],
               ssh_port = int (ssh_cfg['ssh_port']),
               ssh_username = ssh_cfg['ssh_username'],
               ssh_password = ssh_cfg['ssh_password'],
               remote_bind_address = (ssh_cfg['remote_address'], int (ssh_cfg['remote_port'])),
               local_bind_address = (ssh_cfg['local_address'], int (ssh_cfg['local_port']))
              )
    server.start()
    if not server.is_active:
      raise Exception ('ERROR: Cloud not open SSH tunnel !')

    return (server)

  except:
    raise
  
  
# ---------------------------------------------------------------------------
# db_pg_conn ()
# ---------------------------------------------------------------------------
def db_pg_conn (pg_cfg):
  global db_conn

  try:
    db_conn['rdbms'].init (pg_cfg['db_name'], 
                              host = pg_cfg['db_host'],
                              port = int (pg_cfg['db_port']),
                              user = pg_cfg['db_user'],
                              password = pg_cfg['db_pass']
                              )
    db_conn['rdbms'].connect()
    print ('INFO: Connected to database {}.'.format (pg_cfg['db_name']))
    
  except:
    raise Exception ('ERROR: Could not connect to PostgreSQL database {}!'.format (pg_cfg['db_name']))
  
# ---------------------------------------------------------------------------
# db_mongo_conn ()
# ---------------------------------------------------------------------------
def db_mongo_conn (mongo_cfg):
  global db_conn

  try:
    mongo_db = MongoClient (host = mongo_cfg['db_host'],
                            port = int (mongo_cfg['db_port']),
                            username = mongo_cfg['db_user'],
                            password = mongo_cfg['db_pass'],
                            authSource = mongo_cfg['db_name'],
                            authMechanism = 'DEFAULT'
                            )

    print ('INFO: Connected to MongoDB at {}:{}.'.format (mongo_cfg['db_host'], mongo_cfg['db_port']))
    db_conn['nosql'] = mongo_db  

  except Exception as e:
    print (e)
    raise Exception ('ERROR: Could not connect to MongoDB {} at {}:{}!'. \
      format (mongo_cfg['db_name'], mongo_cfg['db_host'], mongo_cfg['db_port']))

# ---------------------------------------------------------------------------
# db_connect ()
# ---------------------------------------------------------------------------
def db_connect ():
  global ssh_tunnel
  try:
    app_cfg = read_app_cfg ()

    # Check config section first
    for value in CONFIG_SECTION_NAMES['mandatory'].values():
      if value not in app_cfg:
        raise Exception ('ERROR: Section [{}] not defined in config file!'.format (value))

    # Open SSH tunnels if needed      
    if 'global' in app_cfg:
      use_ssh_tunnel = app_cfg['global']['use_ssh_tunnel'].capitalize()
      if use_ssh_tunnel in "TrueFalse01" and bool(eval(use_ssh_tunnel)):
        for key in ['rdbms', 'nosql']:
          ssh_section_name = CONFIG_SECTION_NAMES['ssh_tunnel'][key]
          if not ssh_section_name in app_cfg:
            raise Exception ('ERROR: Section {} not defined in config file!'.format (ssh_section_name))
          
          section_name = CONFIG_SECTION_NAMES['mandatory'][key]
          print ('INFO: Opening SSH tunnel for {} ...'.format (section_name.capitalize())) 
          ssh_tunnel[key] = open_ssh_tunnel (app_cfg[ssh_section_name])
    
    # Open database connections
    for key in ['rdbms', 'nosql']:            
      section_name = CONFIG_SECTION_NAMES['mandatory'][key]
      print ('INFO: Connecting to {} database ...'.format (section_name.capitalize()))
      if section_name == 'postgresql':
        db_pg_conn (app_cfg[section_name])
      elif section_name == 'mongodb':
        db_mongo_conn (app_cfg[section_name])
      
  except:
    for value in ssh_tunnel.values():
      value.close ()

    for value in db_conn.values():
      value.close()
          
    raise

