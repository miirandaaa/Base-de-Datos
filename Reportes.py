from Config import *
from Tablas import *
db_conn['rdbms'] = db_conn['rdbms']
def reporte_titular_y_vehiculos():
    with db_conn['rdbms'].atomic():
        reportes = (vehiculo
            .select(vehiculo, propietario_tiene_vehiculo, persona)
            .join(propietario_tiene_vehiculo)
            .join(persona, on=(persona.id_propietario == propietario_tiene_vehiculo.id_propietario))
            .dicts())

        resultado = reportes.execute()
        fila_pasada = None
        for fila in resultado:
            if fila_pasada is None or fila.get('id_propietario') != fila_pasada.get('id_propietario'):
                print(f"\n\033[1mPropietario:\033\n  {fila.get('dni')} – {fila.get('nombres')} {fila.get('apellidos')}\n")
                print(f"    {'Matricula':<15}{'Marca':<15}{'Modelo':<15}{'Color':<15}")
                print(f"    {fila.get('matricula'):<15}{fila.get('marca'):<15}{fila.get('modelo'):<15}{fila.get('color'):<15}")
                fila_pasada = fila
            else:
                print(f"    {fila.get('matricula'):<15}{fila.get('marca'):<15}{fila.get('modelo'):<15}{fila.get('color'):<15}")



def listado_cuenta_con_titular_y_vehiculos():
   with db_conn['rdbms'].atomic():
    reportes = (cuenta
                .select(cuenta, propietario, vehiculo)
                .join(propietario, on=(propietario.id_propietario == cuenta.id_propietario))
                .join(propietario_tiene_vehiculo, on=(propietario_tiene_vehiculo.id_propietario == propietario.id_propietario))
                .join(vehiculo, on=(vehiculo.matricula == propietario_tiene_vehiculo.matricula))
                .dicts())

    resultado = reportes.execute()
    cuenta_pasada = None
    for fila in resultado:
        if cuenta_pasada is None or fila.get('nro_cuenta') != cuenta_pasada.get('nro_cuenta'):
            print(f"Titular: {fila.get('id_propietario')} \nCuenta: {fila.get('nro_cuenta')} {fila.get('saldo')} {fila.get('fecha_creacion_cuenta')}")
            cuenta_pasada = fila
        print(f"Vehiculo: {fila.get('matricula')} {fila.get('marca')} {fila.get('modelo')}")


