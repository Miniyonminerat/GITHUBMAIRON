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

pedir_numero_mes= int(input("Ingresa un numero (mes del año 1/12): "))

diccionario_mes= {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

if pedir_numero_mes in diccionario_mes:

    print("El mes que te toco es:", diccionario_mes[pedir_numero_mes])

else:

    print("El numero que escogiste no esta en el rango esperado")



#------------------------------------------------------------------Ejercicio 10 ------------------------------------------------------------#

#-solicitar un numero de 4 digitos y determina si comienza con 1, 2 o cualquier otro


numero_4_digitos = input("Ingresa un numero: ")  

if numero_4_digitos[0] == "1":


    print("El numero empieza con 1 ")


elif numero_4_digitos[0] == "2":

    print("El numero empieza con 2 ")


else:
    
    print("El numero no comienza ni con 1 ni con 2")




























































