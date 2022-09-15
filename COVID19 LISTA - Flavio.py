
#---------------------------------------------------LISTAS------------------------------------------------------
vacuna = [
       ['Sputnik V',18,2,21],
       ['Covishield',18,2,56],
       ['Sinopharm',18,2,21],
       ['AstraZeneca',18,2,56]
]

persona = [
       ['Machuca','Flavio','12345678','Catamarca 454'],
       ['Fernandez','Maria','76533899','Colon 334'],
       ['Barboza','Alejandro','2156892','Brasil 876'],
       ['Mora','Juana','65432990','Yatay 234'],
]

vacunado = [
       [persona[2], vacuna[2], 1, '23-04-2023'],
       [persona[1], vacuna[1], 2, '01-01-2022'],
       [persona[3], vacuna[0], 2, '01-03-2021'],
       [persona[0], vacuna[3], 1, '03-03-2021'],
]

#---------------------------------------------------FUNCIONES------------------------------------------------

#MOSTRAR LISTAS

def listar_vacunas():  
   print('='*45)
   print('LISTADO DE VACUNAS DISPONIBLES: ')
   print('='*45)
   for vacunas in vacuna:
      print(f'Vacunas: {vacunas[0]}')
      print(f'Edad para vacunar: {vacunas[1]}')
      print(f'Dosis requeridas: {vacunas[2]}')
      print(f'Intervalo entre las dosis: {vacunas[3]} dias')
      print('='*45)

def listar_personas(): 
   print('='*45)
   print('LISTA DE PERSONAS:')
   print('='*45)
   for personas in persona:
      print(f'Registro Nro: {persona.index(personas)+1}')
      print(f'Apellido: {personas[0]}')
      print(f'Nombre: {personas[1]}')
      print(f'DNI: {personas[2]}')
      print(f'Domicilio: {personas[3]}')
      print('='*45)


def listar_vacunados(): 
   for vacunados in vacunado:
      print(f'Registro Nro: {vacunado.index(vacunados)+1}')
      print(f'Apellido: {vacunados[0][0]}')
      print(f'Nombre: {vacunados[0][1]}')
      print(f'DNI: {vacunados[0][2]}')
      print(f'Vacuna: {vacunados[1][0]}')
      print(f'Dosis: {vacunados[2]}')
      print(f'Fecha:{vacunados[3]}')
      print('='*45)

def listar_vacunados1(): 
   print('='*45)
   print('LISTA DE PERSONAS VACUNADAS CON LA 1ER DOSIS') 
   print('='*45)
   for vacunados in vacunado:
      if vacunados[2] == 1:
         print(f'Registro Nro: {vacunado.index(vacunados)+1}')
         print(f'Apellido: {vacunados[0][0]}')
         print(f'Nombre: {vacunados[0][1]}')
         print(f'DNI: {vacunados[0][2]}')
         print(f'Vacuna: {vacunados[1][0]}')
         print(f'Dosis: {vacunados[2]}')
         print(f'Fecha:{vacunados[3]}')
         print('='*45)

def listar_vacunados2(): 
   print('='*45)
   print('LISTA DE PERSONAS VACUNADAS CON LA 2DA DOSIS')
   print('='*45)
   for vacunados in vacunado:
      if vacunados[2] == 2:
         print(f'Registro Nro: {vacunado.index(vacunados)+1}')
         print(f'Apellido: {vacunados[0][0]}')
         print(f'Nombre: {vacunados[0][1]}')
         print(f'DNI: {vacunados[0][2]}')
         print(f'Vacuna: {vacunados[1][0]}')
         print(f'Dosis: {vacunados[2]}')
         print(f'Fecha:{vacunados[3]}')
         print('='*45)

# OPCIONES PARA LISTA DE PERSONAS

def agregar_personas():
   print()
   apellido=input('Ingrese el apellido: ')
   nombre=input('Ingrese el nombre: ')
   dni=input('Ingrese el DNI: ')
   domicilio=input('Ingrese el domicilio: ')
   persona.append([apellido, nombre, dni, domicilio])

def eliminar_personas():
   listar_personas()      
   print()
   resp=int(input('Ingrese el numero del resgistro que desea eliminar: '))
   vacuna.pop(resp-1)
   print('Persona eliminada exitosamente')

def modificar_personas():
   listar_personas()      
   print()
   modi1=input('Ingresar el numero de dni: ') 
   for personas in persona:
      if modi1 == personas[2]:
         print('¿Que datos desea cambiar?')
         print()
         print('1-Apellido')
         print('2-Nombre')
         print('3-DNI')
         print('4-Dirección')
         print()
      rtam1=input('Ingrese el Nro: ')
      if rtam1=='1':
         personas[0]=input('Ingrese el nuevo apellido: ')
      elif rtam1 == '2':
         personas[1]=input('Ingrese nuevo nombre: ')
      elif rtam1 =='3':
         personas[2]=input('Ingrese nuevo DNI: ')
      elif rtam1 =='4':
         personas[3]=input('Ingrese nueva direccion: ') 
      else:
         print(f'no se encontro.') 

#OPCIONES PARA LISTA DE VACUNADOS

def agregar_vacunados():
   listar_vacunados()
   print()
   for vacunados in vacunado:
      persD=input('Ingrese dni: ')
      encontro = False
   for item in persona:
      if persD == item[2]:
         encontro = True
         posicion=persona.index(item)
      if encontro == False:
         persA=input('Ingrese el Apellido: ')
         persN=input('Ingrese el nombre: ')
         persdd=input('Ingrese domicilio')
         persona.append([persA,persN,persD,persdd])
         posicion=len(persona)-1
   for item in vacuna:
      print(vacuna.index(item),item[0])
      persV=int(input('Ingrese el numero de vacuna: '))
      persDS=input('Ingrese dosis')
      persF=input('Ingrese fecha')
      vacunado.append([persona[posicion],vacuna[persV],persDS,persF])
      print(vacunado[len(vacunado)-1])
      print('Persona agregada exitosamente')
      a=input('Desea agregar otra persona presione S')
      if a == 's':
         print('Agrege otra persona')
      else: 
         print('Gracias')
         break

def eliminar_vacunado():
   listar_vacunados()   
   print()
   resp1=int(input('Ingrese el numero del resgistro que desea eliminar: '))
   vacunado.pop(resp1-1)
   print('Persona eliminada exitosamente')

def modificar_vacunado():
   listar_personas()
   listar_vacunados()
   listar_vacunas()      
   print()
   modi2=input('Ingresar el DNI de la persona: ')
   for personas in persona:
      if modi2 == personas[2]:
         print('¿Que datos desea cambiar?')
         print()
         print('1-Modificar el apellido: ')
         print('2-Modificar el nombre: ')
         print('3-Modificar la vacuna: ')
         print('4-Ingrese nueva dosis: ')
         print('5-Ingrese nueva fecha: ')
         print()
         rtam2=input('Ingrese el Nro: ')
         if rtam2=='1':
            personas[0]=input('Ingrese el nuevo apellido: ')
         elif rtam2 == '2':
            personas[1]=input('Ingrese nuevo nombre: ')
   for vacunas in vacuna:
         if rtam2 == '3':
               vacuna[0]=input('Ingrese la vacuna aplicada: ')
   for vacunados in vacunado: 
            if rtam2 == '4':
               vacunado[2]=int(input('Ingrese la nueva dosis aplicada: '))
            elif rtam2 == '5': 
               vacunado[3]=input('Ingrese la nueva fecha: ') 
            else:
                print('MODIFICACIÓN REALIZADA')  
      
            
#-----------------------------------------PANTALLA PRINCIPAL------------------------------------
print('                    BIENVENIDO                       ')
print('Al programa de gestion de vacunacion contra el COVID-19')

while True:
   print()
   print('Ingrese el numero de la lista que desea mirar: ')
   print()
   print('1- Lista de Vacunas Disponibles.')
   print('2- Lista de Personas Registradas.') 
   print('3- Lista de Personas Vacunas con la 1er Dosis.')
   print('4- Lista de Personas Vacunas con la 2da Dosis.')
   print()
   print('Opciones para lista de personas:')
   print()
   print('5- Agregar una persona.')
   print('6- Modificar datos del registro de personas listadas.')
   print('7- Eliminar datos del registro de personas.')
   print()
   print('Opciones para la lista de personas vacunadas:')
   print()
   print('8- Agregar una persona al registro.')
   print('9- Modificar datos del registro de personas.')
   print('10- Eliminar persona del registro.')
   print()
   respuesta=input('Ingrese el numero de la lista: ')
   print('Ingresaste el número: ', respuesta)
   if respuesta =='1':
      listar_vacunas()
   elif respuesta =='2':
      listar_personas()
   elif respuesta =='3':
      listar_vacunados1()
   elif respuesta =='4':
      listar_vacunados2()
   elif respuesta =='5':
      agregar_personas()
   elif respuesta == '6':
      modificar_personas()      
   elif respuesta == '7':
      eliminar_personas()  
   elif respuesta == '8':
      agregar_vacunados() 
   elif respuesta == '9':
      modificar_vacunado()     
   elif respuesta == '10':
      eliminar_vacunado()   
   rp= input('Desea realizar otra operación presione S: ')
   if rp.upper() != 'S':
    print('¡Gracias por utilizar el programa!')
    break
   
    
