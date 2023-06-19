from Tablas import *
from Config import *
from Cuenta import *
import datetime

def acreditacion():
    with db_conn['rdbms'].atomic():
        try:
            cuenta_acred = cuenta.get_or_none(cuenta.nro_cuenta == int(input("Ingrese el numero de cuenta a acreditar saldo: ")))

            if cuenta_acred:
                monto_acred = int(input("Ingrese monto a acreditar: "))
                credito.create(nro_cuenta = cuenta_acred, fecha_hora_credito = datetime.now, importe_credito = monto_acred)
                db_conn['rdbms'].commit()
                print('Acreditación exitosa.')
    
        except IntegrityError():
            db_conn['rdbms'].rollback()
            print("Error: No se pudo realizar la acreditación.")
    
    