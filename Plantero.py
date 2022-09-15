def calcular_extra(t):
  if t>25:
   return 20
  elif t>20 and t<=25:
   return 10 
  elif t>10 and t<=20:
   return 5 
  else: 
   return 0

print('Calculador de riego de plantines')
print('         ')
print('---------------------------------')
print('         ')

print('Lista de especies de plantas')

listab = [
       ['tomate',96],
       ['lechuga',74],
       ['zanahoria',89],
       ['mandioca',76]
]

print('           ')
print('--------------------------------')

print('           ')
temp = int(input('Ingrese la temperatura en grados celsius: '))
agua_extra= calcular_extra(temp) 

print('Agua extra a utlizar: ', str(agua_extra))

for elemento in listab:
 print('plantas: ' ,elemento[0],' Agua requerido: ' ,elemento[1]+agua_extra)


