print('*** Suma Acumulativa ***')

# Sumar los primeros 5 numeros
MAX = 5000
num = 1
aux_sum = 0

# Empezamos a iterar
while num <= MAX:
    # Imprimir lo que se va a sumar
    print(f'(acumulador_suma + numero) -> {aux_sum} + {num}')

    aux_sum += num
    num += 1

    # Imprimir el resultado de la suma parcial
    print(f'Suma parcial acumulada: {aux_sum}\n')

print(f'\nResultado suma acumulada: {aux_sum}')