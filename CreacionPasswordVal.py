#Validdacion y creacion de password

print('--> Creación y Validación de un Password <--')

pas = input('Ingresa un password (debe tener al menos 6 caracteres: ')

# Validar el password
while len(pas) < 6:
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracteres')
    pas = input('Ingresa un nuevo valor de password: ')
else:
    print('El valor de password es válido')
