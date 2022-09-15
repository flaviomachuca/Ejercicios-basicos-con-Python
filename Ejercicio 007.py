#Ejercicio 007
#Solicitar al usuario el ingreso de tres números cualquiera, luego realizar las siguientes operaciones:
#• calcular y mostrar la suma de los dos valores más grandes.

print('Operacion Nro 1')
n1=int(input('Ingrese un numero: '))
n2=int(input('Ingrese un numero: '))
n3=int(input('Ingrese un numero: '))
valor1 = n1 + n2 + n3
print(valor1)

print('Operacion Nro 2')
n4=int(input('Ingrese un numero: '))
n5=int(input('Ingrese un numero: '))
n6=int(input('Ingrese un numero: '))
valor2 = n4 + n5 + n6
print(valor2)

print('Operacion Nro 3')
n7=int(input('Ingrese un numero: '))
n8=int(input('Ingrese un numero: '))
n9=int(input('Ingrese un numero: '))
valor3 = n7 + n8 + n9
print(valor3)

a=max(valor1, valor2, valor3)
b=min(valor1, valor2, valor3)
c=(valor1 + valor2 + valor3)- a - b

print('Los valores mas altos son', a, c, b)
