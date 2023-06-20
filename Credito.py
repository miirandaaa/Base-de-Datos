from Tablas import *
from Config import *
from Cuenta import *
from datetime import datetime

def acreditacion():
    with db_conn['rdbms'].atomic():
        try:
            nro_cuenta_acred = int(input("Ingrese el numero de cuenta a acreditar saldo: "))
            cuenta_acred = cuenta.get_or_none(cuenta.nro_cuenta == nro_cuenta_acred)

            if cuenta_acred:
                monto_acred = int(input("Ingrese monto a acreditar: "))
                fecha_hora_actual = datetime.now()
                credito.create(nro_cuenta = cuenta_acred, fecha_hora_credito = fecha_hora_actual, importe_credito = monto_acred)
                
                cuenta_a_acreditar = cuenta.get_by_id(nro_cuenta_acred)
                saldo_pasado = cuenta_a_acreditar.saldo
                nuevo_saldo = int(saldo_pasado + monto_acred)
                modificar_cuenta(nro_cuenta_acred,nuevo_saldo)
                print('Acreditación exitosa.')
        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo realizar la acreditación.")
    
    