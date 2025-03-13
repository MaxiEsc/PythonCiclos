print('--> Repetición de un Mensaje <--')

men = input('Proporciona un mensaje a repetir: ')
rep = int(input('Proporciona el número de repeticiones: '))

# Iterar sobre el rango de repeticiones
#Podemos ahorrarnos la creacion de variables en Python dentro del ciclo FOR con la notacion _ en lugar de completar con
#con la clasica iteracion i
for _ in range(rep):
    # print(f'{i+1} - {mensaje}')
    print(men)
