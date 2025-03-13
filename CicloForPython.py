#Interesante forma de realizar el ciclo for en Python

print('*** Ciclo for ***')

print('Recorremos los caracteres de una cadena')
cadena = 'Hola Mundo'
# iteramos los caracteres y cadenas (Que en realidad es un arreglo)
for letra in cadena:
    print(letra, end=' ')

print('\n\nRecorremos la lista de frutas:')
#Concepto de arreglos y listas
frutas = ['Plátano', 'Fresa', 'Mango']
for fruta in frutas:
    print(fruta, end=' ')