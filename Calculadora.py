#Calculadora en consola con Python y un sistema de menu
print('--> Calculadora en Python <--')
op1 = op2 = res = 0
salir = False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Suma 
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir''')
    op = int(input('Escoje una opción: '))
    # Vamos a solicitar el valor de los operandos
    if 1 <= op <= 4:
        op1 = float(input('Dame el valor 1: '))
        op2 = float(input('Dame el valor 2: '))
    # Revisamos el tipo de operación a realizar
    if op == 1:  # Suma
        res = op1 + op2
        print(f'El resultado de la suma es: {res:.2f}\n')
    elif op == 2:  # Resta
        res = op1 - op2
        print(f'El resultado de la resta es: {res:.2f}\n')
    elif op == 3:  # Multiplicacion
        res = op1 * op2
        print(f'El resultado de la multiplicación es: {res:.2f}\n')
    elif op == 4:
        res = op1 / op2
        print(f'El resultado de la divión es: {res:.2f}\n')
    elif op == 5:
        print(f'Saliendo del programa de Calculadora. Hasta pronto!')
        salir = True
    else:
        print(f'Opción inválida, selecciona otra opción...\n')