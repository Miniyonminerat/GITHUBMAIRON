#------------------------------------------------------------------Ejercicio 1 ------------------------------------------------------------#

#-pedir edad y definir si es menor de edad mayor de edad o adulto mayor


# pedir_edad= int(input("Ingresa tu edad: "))



# if pedir_edad < 18: 

#     print(f"Usted es menor de edad por que tiene {pedir_edad} ")

# elif pedir_edad >= 18:
    
#     print(f"Usted es mayor de edad por que tiene {pedir_edad} ")

# elif pedir_edad >= 65:
    
#     print(f"Usted es un adulto mayor por que tienes {pedir_edad}")


#------------------------------------------------------------------Ejercicio 2 ------------------------------------------------------------#

#-pedir estarura y definir si es pequeño mediano o alto


# pedir_estatura= float(input("Ingresa tu estatura actual: "))


# if pedir_estatura < 1.5:

#     print(f"Eres considerado bajito, jajaja enano ")

# elif pedir_estatura > 1.5 and pedir_estatura <= 1.9:

#     print(f"Tienes una estatura mediana eres normal :D ")

# else:

#     print(f"Eres demasiado alto pareces girafa que tal el clima arriba? ")


#------------------------------------------------------------------Ejercicio 3 ------------------------------------------------------------#

#-pedir numero y mirar si es multiplo de 2 y de 3


# pedir_numero= float(input("Ingresa un numero: "))



# if pedir_numero % 2 == 0 and pedir_numero % 3 == 0: 

#     print("Tu numero es multiplo de 2 y de 3 al mismo tiempo")

# else:

#     print("Tu numero no es multiplo de 3 ni de 2 al mismo tiempo :v")



#------------------------------------------------------------------Ejercicio 4 ------------------------------------------------------------#

#- pedir numero decimal y determinar si tiene 1, 2 o mas de 2 decimales  usar str y split


# pedir_decimal = input("Ingrese un número decimal: ")

# partes = pedir_decimal.split(".")

# if len(partes) == 2:


#     decimales = partes[1]
    
#     cantidad = len(decimales)

#     if cantidad == 1:


#         print("Tiene 1 decimal")

#     elif cantidad == 2:


#         print("Tiene 2 decimales")

#     else:
#         print("Tiene más de 2 decimales")

# else:

#     print("No tiene decimales")


#------------------------------------------------------------------Ejercicio 5 ------------------------------------------------------------#

#-pedir un pais y mostrar si esta en la siguiente tupla: ("Colombia", "Peru", "Argentina", "Mexico")

# pedir_pais= input("Ingresa un pais y verificar si esta en la tupla: ")


# tupla_pais= ("Colombia", "Peru", "Argentina", "Mexico")

# if pedir_pais in tupla_pais:
    
#     print(f"Tu pais esta en la tupla y es {pedir_pais}")

# else:

#     print(f"Tu pais no esta en la tupla y es {pedir_pais}")


#     print(f"La tupla era: {tupla_pais}")




#------------------------------------------------------------------Ejercicio 6 ------------------------------------------------------------#

#-Pedir tipo de sangre (A, B, AB, O) y muestra tu compatibilidad segun un diccionario predefinido


# pedir_sangre= input("Ingrese su tipo de sangre (A, B, AB, O) :")

# diccionario_sangres_compatibles= {

#     "A":"Puede donar a A y AB Puede recibir de A y O",
#     "B":"Puede donar a B y AB Puede recibir de B y O",
#     "AB":"Puede donar a AB puede recibir de todos los existentes",
#     "O":"Puede donar a todos puede recibir de solo O"



# }

# if pedir_sangre in diccionario_sangres_compatibles:
    
#     print("Compatibilidad:", diccionario_sangres_compatibles[pedir_sangre])

# else:

#     print("Esa sangre no existe que pedo extraterrestre :O")


#------------------------------------------------------------------Ejercicio 7 ------------------------------------------------------------#

#-Pedir temperatura en grados °C si es menor de 10 hace frio si esta entre 10 y 25 esta templado y mas de 25 hace calor 

# pedir_temperatura= float(input("Ingresa la temperatura actual en °C: "))


# if pedir_temperatura <10:

#     print("Hace frio acobijese y duermase no se levante :V ")

# elif pedir_temperatura >= 10 and pedir_temperatura <= 26:

#     print("Esta templado levantese y vaya haga algo por su vida ")

# else:

#     print("Esta haciendo calor saquese unos hielos y tirese al suelo con el ventilador ;c ")



#------------------------------------------------------------------Ejercicio 8 ------------------------------------------------------------#

#-crear un menu con opciones 1 suma 2 resta 3 multiplicar pedir 2 numeros y ejecuta la operacion seleccionada

# numero_operacion= float(input("Ingresa un numero para hacer operacion: "))

# numero_operacion_2= float(input("Ingresa un numero para hacer operacion: "))


# print(""" MENU DE OPERACIONES 
#      1. SUMA 
#      2. RESTA
#      3. MULTIPLICACION""")

# escoja= input("Escoja que operacion quiere hacer: ")

# if escoja == "1":

#     operacion_suma= numero_operacion + numero_operacion_2

#     print(f"Su operacion esta completada es: {operacion_suma}")


# elif escoja == "2":

#     operacion_resta= numero_operacion - numero_operacion_2

#     print(f"Su operacion esta completada su resultado fue: {operacion_resta}")

# elif escoja == "3":

#     operacion_multiplicacion= numero_operacion * numero_operacion_2

#     print(f"Su operacion esta hecha su resultado final fue: {operacion_multiplicacion}")

# else:

#     print("Escojiste un numero no en el menu reinicia y vuelve a intentar: ")



#------------------------------------------------------------------Ejercicio 9 ------------------------------------------------------------#

#-pedir un numero entre 1 y 12 y muestra el mes correspondiente usando un diccionario

# pedir_numero_mes= int(input("Ingresa un numero (mes del año 1/12): "))

# diccionario_mes= {
#     1:"Enero",
#     2:"Febrero",
#     3:"Marzo",
#     4:"Abril",
#     5:"Mayo",
#     6:"Junio",
#     7:"Julio",
#     8:"Agosto",
#     9:"Septiembre",
#     10:"Octubre",
#     11:"Noviembre",
#     12:"Diciembre"
# }

# if pedir_numero_mes in diccionario_mes:

#     print("El mes que te toco es:", diccionario_mes[pedir_numero_mes])

# else:

#     print("El numero que escogiste no esta en el rango esperado")



# #------------------------------------------------------------------Ejercicio 10 ------------------------------------------------------------#

# #-solicitar un numero de 4 digitos y determina si comienza con 1, 2 o cualquier otro


# numero_4_digitos = input("Ingresa un numero: ")  

# if numero_4_digitos[0] == "1":


#     print("El numero empieza con 1 ")


# elif numero_4_digitos[0] == "2":

#     print("El numero empieza con 2 ")


# else:
    
#     print("El numero no comienza ni con 1 ni con 2")


#------------------------------------------------------------------Ejercicio 11 ------------------------------------------------------------#

#- Ingresa una palabra. Muestra su primera letra es vocal, consonante o un numero

# primera_letra= input("Ingresa una palabra: ")

# primera_letra_buscar= primera_letra[0]

# vocales_en_mayusculas= "AEIOU"


# vocales_en_minuscula= "aeiou"


# numeros= "0123456789"

# if primera_letra_buscar in numeros:

#     print(f"La palabra tiene de primero un numero que es {primera_letra[0]} ")

# elif primera_letra_buscar in vocales_en_mayusculas or primera_letra_buscar in vocales_en_minuscula:

#     print(f"La palabra tiene de primero la vocal {primera_letra[0]}")

# else:

#     print(f"La primera letra es consonante y es {primera_letra[0]}")


#------------------------------------------------------------------Ejercicio 12 ------------------------------------------------------------#

#-pide una fruta. si esta en la lista ["manzana" , "pera" , "piña"], muestra su precio. Si no, indica que no esta disponible

# lista_fruta= ["manzana" , "pera" , "piña"]


# pedir_fruta= input("Ingresa una fruta si esta disponible se le da el precio: ")


# if pedir_fruta == "manzana":

#     print("La manzana vale 3500 pesos pague ya ")

# elif pedir_fruta == "pera":

#     print("La pera vale 2300 pesos esta barata comprela ya :p")

# elif pedir_fruta == "piña":

#     print("La piña vale 5000 llevela que esta jugosa apenas pa un juguito :D")    

# else:

#     print(f"Perdon no hay esa fruta pero hay {lista_fruta} puede pedir cualquiera de esas compreme porfa ;v ")


#------------------------------------------------------------------Ejercicio 13 ------------------------------------------------------------#

#-pide tu calificacion (0 a 5) si es menor que 3 reprobo si esta entre 3 y 4 aprobado mayor que 4 excelente


# pedir_calificacion= float(input("Ingresa tu calificacion del periodo (posata ojala pases o si no chacletaso): "))


# if pedir_calificacion < 3:

#     print("Perdiste esta materia tan facil te ganaste un chancletaso a recuperar")

# elif pedir_calificacion >= 3 and pedir_calificacion <= 4:

#     print("Pasaste regular te salvaste por un pelo del chancletaso ")

# else:

#     print("Eres buen estudiante no se como piensan darte chancletaso felicidades el mejor :O")   




#------------------------------------------------------------------Ejercicio 14 ------------------------------------------------------------#

#-pide un numero y muestra si es divisible entre 4, entre 6 o no lo es

# numero_divisible_2= float(input("Ingresa un numero si es divisible entre 4 o entre 6: "))

# if numero_divisible_2 % 4 == 0 and numero_divisible_2 % 6 == 0:

#     print("El numero que escogiste es divisible entre 4 y 6 ")



# elif numero_divisible_2 % 4 == 0:

#     print("El numero que escogiste si es divisible entre 4 no entre 6")

# elif numero_divisible_2 % 6 == 0:

#     print("El numero que escogiste si es divisible entre 6 pero no entre 4")

# else: 

#     print("El numero no es divisible ni por 4 no por 6 ")



#------------------------------------------------------------------Ejercicio 15 ------------------------------------------------------------#


#- Crea un sistema de autenticacion basico. pide usuario y contraseña usa un diccionario para validar


# diccionario_usuarios = {

#     "admin": "1234",
#     "usuario1": "abcd",
#     "mairon": "clave"
# }

# usuario_nombre_pedir = input("Ingresa tu usuario: ")

# contraseña = input("Ingresa tu contraseña: ")

# if usuario_nombre_pedir in diccionario_usuarios and diccionario_usuarios[usuario_nombre_pedir] == contraseña:

#     print("Acceso permitido.")

# else:

#     print("Usuario o contraseña incorrectos.")


#------------------------------------------------------------------Ejercicio 16 ------------------------------------------------------------#

#-Solicia una edad y muestra a que grupo pertenece: niño (0-12) adolecente (13-17) adulto (18-64) mayor (65+)


# edad_persona = int(input("Por favor, ingresa tu edad: "))

# limite_edad_nino = 12


# limite_edad_adolescente = 17


# limite_edad_adulto = 64



# if edad_persona >= 0 and edad_persona <= limite_edad_nino:


#     print("Grupo: Niño")

# elif edad_persona <= limite_edad_adolescente:


#     print("Grupo: Adolescente")

# elif edad_persona <= limite_edad_adulto:


#     print("Grupo: Adulto")

# elif edad_persona >= 65:


#     print("Grupo: Adulto Mayor")

# else:

#     print("Edad no válida.")



#------------------------------------------------------------------Ejercicio 17 ------------------------------------------------------------#

#-Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra "ciudad secundaria".

# ciudad_ingresada = input("Ingresa el nombre de una ciudad: ")


# ciudades_capitales = ("Bogotá", "Lima", "Quito", "Buenos Aires", "Santiago")


# if ciudad_ingresada in ciudades_capitales:

#     print("Es una ciudad capital.")

# else:
#     print("Ciudad secundaria.")


# #------------------------------------------------------------------Ejercicio 18 ------------------------------------------------------------#


# #Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de descuento.Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay descuento.

# valor_compra = float(input("Ingresa el valor de la compra: "))

# if valor_compra > 200000:


#     descuento = valor_compra * 0.15

# elif valor_compra >= 100000:

#     descuento = valor_compra * 0.10

# else:

#     descuento = 0

# valor_final = valor_compra - descuento

# print("El valor final de la compra es:", valor_final)


# #------------------------------------------------------------------Ejercicio 19 ------------------------------------------------------------#


# #-Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa de $10.000/hora.Si trabajó más de 40 horas, aplica un bono del 20%.

# nombre_empleado = input("Ingresa tu nombre: ")


# horas_trabajadas = int(input("Ingresa el número de horas trabajadas: "))

# tarifa_por_hora = 10000

# salario_base = horas_trabajadas * tarifa_por_hora


# if horas_trabajadas > 40:

#     bono = salario_base * 0.20

# else:

#     bono = 0


# salario_total = salario_base + bono

# print("Empleado:", nombre_empleado)


# print("Salario total:", salario_total)


# #------------------------------------------------------------------Ejercicio 20 -------------------------------------------------------------#

# # Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente.De 50 a 79, aceptable. 80 a 100, sobresaliente.

# puntaje_prueba = int(input("Ingresa tu puntaje (0 a 100): "))

# if puntaje_prueba < 50:

#     print("Insuficiente")

# elif puntaje_prueba <= 79:

#     print("Aceptable")
# else:

#     print("Sobresaliente")










