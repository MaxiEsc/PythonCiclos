print('*** Aplicación de Cajero Automático ***')

monto = 1000
fin = False
while not fin:
    print(f'''Operaciones que puedes realizar:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    op = int(input('Escoje una opción: '))
    if op == 1:
        print(f'Tu saldo actual es: ${monto:.2f}\n')
    elif op == 2:
        saldo = float(input('Ingresa el monto a retirar: '))
        # Validacion
        if saldo <= monto:
            monto -= saldo  # saldo = saldo - retiro
            print(f'Tu nuevo saldo es: ${monto:.2f}\n')
        else:
            print(f'No cuentas con el saldo suficiente. Saldo actual es: ${monto:.2f}\n')
    elif op == 3:
        deposito = float(input('Ingresa el monto a depositar: '))
        monto += deposito  # saldo = saldo + deposito
        print(f'Tu nuevo saldo es: ${monto:.2f}\n')
    elif op == 4:
        print(f'Saliendo del cajero automático. Hasta pronto!')
        fin = True
    else:
        print('Opción inválida. Selecciona otra opción\n')
else:
    print('Terminando la aplicación de Cajero Automático!')