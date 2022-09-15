#Ejercicio 009
#Por encargo de una empresa inmobiliaria, se necesita un algoritmo para calcular el presupuesto de
#materiales para obras albañilería de mantenimiento en edificios, según los metros cuadrados a reparar.
#Los materiales a integrar en el presupuesto son los siguientes: ladrillos, cemento y arena.
#Para el cálculo, se debe preguntar al usuario la cantidad de metros cuadrados sobre los que se deberá
#calcular el presupuesto, y el costo por metro cuadrado de construcción de estos materiales.
#Finalmente, se deberá mostrar al usuario el resultado del cálculo del presupuesto respetando el siguiente
#formato (en las distintas partes en que figure “ xxxxx ”, deberá aparecer el valor correspondiente de acuerdo a
#la información ingresada por el usuario y a los cálculos realizados):
print('-----------------------------')
print('PRESUPUESTO DE MANTENIMIENTO')
print('-----------------------------')

metros=int(input('Ingrese los metros cuadrados: '))

print('Precio de materiales por metro cuadrado:')
ladrillo= int(input('Ladrillo: $'))
cemento=int(input('Cemento: $'))
arena= int(input('Arena: $'))

calculol= ladrillo / metros
calculoc=cemento / metros
calculoa=arena / metros 
costo= calculol+calculoc+calculoa

print(' ')
print('Costo total de materiales:')
print('Total ladrillo: $', str(calculol))
print('Total cemento: $', str(calculoc))
print('Total arena: $',str(calculoa))
print('                                  ')
print('IMPORTE TOTAL DE OBRA: $', str(costo))

