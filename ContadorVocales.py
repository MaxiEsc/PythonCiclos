# Declarar la variable
cont_voc= 0
palabra = 'Hola Mundo'
# Agregar el ciclo for
for e in palabra:
    if e == 'a' or e == 'e' or e == 'i' or e == 'o' or e == 'u':
        cont_voc = cont_voc + 1
# Imprimir la cantidad de vocales encontradas en la cadena
print(f'la cantidad de vocales encontradas son {cont_voc} en total')