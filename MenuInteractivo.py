# Al fin se practica uno de los menu hecho con do while pero en este caso es con while

print('--> Sistema de Administración de Cuentas <-- ')

fin = False
while not fin:
    print(f'''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    op = int(input('Escoje una opción: '))
    if op == 1:
        print('Creando tu cuenta...\n')
    elif op == 2:
        print('Eliminado tu cuenta...\n')
    elif op == 3:
        print('Saliendo del sistema. Hasta pronto!\n')
        fin = True
    else:
        print('Opción inválida, proporciona otra opción...\n')
else:
    print('Terminando el sistema de Administración de Cuentas')