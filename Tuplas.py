#-------------------------------------------------------------Tupla ejercicio inicio ejemplo----------------------------------------------------#

#-Pasar tupla a lista-#

#  la_tupla= (1, 2, 3)

#  la_lista = list(la_tupla)

#  print(la_lista)


#-Convertir lista a tupla-#

#  una_lista= ["uno", "dos", "tres"]


#  otra_tupla= tuple(una_lista)


#  print(otra_tupla)




# -------------------------------------------------------------Tupla ejercicio 1----------------------------------------------------#


# tupla_frutas= ("manzana", "pera")

# tupla_a_lista= list(tupla_frutas)

# fruta_teclado= input("Ingresa una fruta: ")

# tupla_a_lista.append(fruta_teclado)

# lista_a_tupla= tuple(tupla_a_lista)

# print(f"las frutas que tienes organizadas en tu carro de mercado son: {lista_a_tupla}")




# -------------------------------------------------------------Tupla ejercicio 2----------------------------------------------------#


# tupla_calificaciones= (4.2, 3.8)

# tupla_a_lista_2= list(tupla_calificaciones)

# nota_teclado= float(input("Ingresa una nota: "))

# tupla_a_lista_2.append(nota_teclado)

# lista_a_tupla_2= tuple(tupla_a_lista_2)

# print(f"Tus calificaciones estan organizadas de esta manera y no se pueden cambiar {lista_a_tupla_2}: ")




# -------------------------------------------------------------Tupla ejercicio 3----------------------------------------------------#

# tupla_nombre= ("Ana", "Gomez")

# tupla_a_lista_3= list(tupla_nombre)

# nombre_teclado= int(input("Ingresa tu numero de documento: "))

# tupla_a_lista_3.append(nombre_teclado)

# lista_a_tupla_3= tuple(tupla_a_lista_3)

# print(f"Tu documento esta organizado de esta manera: {lista_a_tupla_3} bienvenida")


# -------------------------------------------------------------Tupla ejercicios otros 1----------------------------------------------------#

#CREAR TUPLA CON NUMEROS DEL 1 AL 5




tupla_numeros= (1, 2, 3, 4, 5)


#-IMPRIME LA TUPLA

print(f"Los numeros de tu tarjeta de credito son: {tupla_numeros}")


# -------------------------------------------------------------Tupla ejercicios otros 2----------------------------------------------------

#POSICION DEL SEGUNDO NUMERO DE LA TUPLA



tupla_numeros.index(2)



#- IMPRIME LA POSICION DEL SEGUNDO NUMERO DE LA TUPLA 

print(f"La posicion del segundo numero de la tupla es: {tupla_numeros.index(2)}")

# -------------------------------------------------------------Tupla ejercicios otros 3----------------------------------------------------

#OBTENER CUANTOS ELEMENTOS TIENE LA TUPLA

len(tupla_numeros)

#- IMPRIME EL RESULTADO DE LOS ELEMENTOS TOTALES QUE TIENE LA TUPLA

print(f"Los elementos que tiene la tupla son: {len(tupla_numeros)}")


# -------------------------------------------------------------Tupla ejercicios otros 4----------------------------------------------------

#ENCONTRAR A POSICION DEL NUMERO 4 EN LA TUPLA

tupla_numeros.index(4)

#-IMPRIME RESULTADO DE LA POSICION EXACTA DE EL NUMERO 4 EN LA TUPLA

print(f"Tu posicion del numero 4 es: {tupla_numeros.index(4)}")


# -------------------------------------------------------------Tupla ejercicios otros 5----------------------------------------------------

#- SE USA LA TUPLA DE LOS NUMEROS Y SE USA EL .COUNT PARA CONTAR CUANTAS VECES APARECE EL NUMERO 2 EN LA TUPLA

tupla_numeros.count(2)

#- SE IMPRIME EL RESULTADO PARA SABER CUAL ES EL VALOR DE EL .COUNT CON LA REPETICION DEL NUMERO 2

print(f"El valor que se conto es: {tupla_numeros.count(2)}")


# -------------------------------------------------------------Tupla ejercicios otros 6----------------------------------------------------


#-SE CREA UNA TUPLA CON STRING, INT, FLOAT

tupla_variada= ("juanito", 30, 5.1 )

#-SE IMPRIME LE TUPLA VARIADA

print(f"estos son tus resultados de la tupla: {tupla_variada}")




# -------------------------------------------------------------Tupla ejercicios otros 7----------------------------------------------------


#- CREAR UNA TUPLA QUE CONTIENE OTRA TUPLA

tupla1= (23, 44, ("pepito", 45), "Tu", "tupla")

#- SE ACCEDE AL PRIMER VALOR DE LA TUPLA

tupla_interna = tupla1[2][0]

#- SE IMPRIME EL PRIMER VALOR DE LA TUPLA

print(f"El valor primario de la tupla interna es: {tupla_interna}")
















