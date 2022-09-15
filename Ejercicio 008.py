#Ejercicio 008
#Solicitar al usuario que ingrese su nombre y su edad. Luego mostrar por consola uno de los siguientes
#mensajes, dependiendo de la edad ingresada por el usuario:
#• “Hola xxxxxx, como tienes nn años eres MAYOR de edad”
#• “Hola xxxxxx, como tienes nn años eres MENOR de edad”
#Donde “xxxxxx” representa el nombre ingresado por el usuario y “nn” su edad.

usuario=input('Ingrese su Nombre y Apellido: ')
edad= int(input('Ingrese su edad: '))
n=18

if edad > 18: 
    print('Hola', usuario , 'como tienes', edad, 'años eres MAYOR de edad.') 
else:
    print('Hola', usuario , 'como tienes', edad, 'años eres MENOR de edad.')
    
