#Utilizamos una biblioteca de numero random, e intentamos adivinar un numero.
from random import randint

print('--> Juego de Adivinanzas <--')

num_secreto = randint(1, 50)
retry = 0
adiv = None
INT_MAX = 5

while adiv != num_secreto and retry < INT_MAX:
    adiv = int(input('Adivina el número secreto (1-50): '))
    # Agregamos una ayuda para orientar al jugador
    if adiv < num_secreto:
        print('El número secreto es mayor')
    elif adiv > num_secreto:
        print('El número secreto es menor')
    # Incrementamos la variable de intentos
    retry += 1
# Conclusion del juego
if adiv == num_secreto:
    print(f'Felicidades, adivinaste el número secreto en {retry} intentos')
else:
    print(f'Lo siento, has agotado tus intentos máximos: {INT_MAX}')
    print(f'El número secreto era: {num_secreto}')