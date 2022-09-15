#Ejercicio 006
#Solicitar al usuario el ingreso de tres números cualquiera, luego realizar las siguientes operaciones:
#• calcular y mostrar el valor promedio de estos números
#• calcular y mostrar la suma de los números al cuadrado (suma de los cuadrados)


#n1=int(input('Ingrese un numero:'))
#n2=int(input('Ingrese un numero:'))
#n3=int(input('Ingrese un numero:'))

#val=n1+n2+n3
#print('la suma es:', val)

contador = 0
suma = 0
numero = 0

while numero !=0:
    numero = int(input('Digite un numero entero(O para terminar): '))
    if numero !=0:
     suma += numero
     contador += 1

if contador == 0:
    print('No digito ningun numero.')
else:
    promedio = suma / contador
    print('El promedio de los {} nuemro es igual {}.'. format(contador, promedio))
