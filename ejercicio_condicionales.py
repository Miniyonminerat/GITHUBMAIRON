# # #----------------------------------------Ejercicio 1_condicionales-----------------------------------------#

# # #-Verificar si un numero es mayor o menor o cero

# # numero= float(input("Ingresa un numero: "))

# # if numero > 0:
# #     print(f"El numero es positivo ({numero})")

# # elif numero < 0:
# #     print(f"El numero es negativo ({numero})")

# # else:
# #     print("El numero es cero")
    

# # #----------------------------------------Ejercicio 2_condicionales-----------------------------------------#

# # #-calcula el mayor de 2 numeros ingresados


# # numero_1= float(input("Ingresa un numero: "))

# # numero_2= float(input("Ingresa ultimo numero: "))

# # if numero_1 > numero_2: 
# #     print(f"El numero {numero_1} es mayor que el numero {numero_2}")

# # elif numero_1 < numero_2:
# #     print(f"El numero {numero_1} es menor que el numero {numero_2}")
# # else:
# #     print("Los numeros son iguales")


# # #----------------------------------------Ejercicio 3_condicionales-----------------------------------------#

# # #-Determina si un numero es par o inpar

# # numero_3= int(input("Ingresa un numero: "))

# # if numero_3 % 2 == 0:
# #     print(f"El numero ingresado es par({numero_3})")

# # else:
# #     print(f"El numero es inpar({numero_3})")

    
# # #----------------------------------------Ejercicio 4_condicionales-----------------------------------------#

# # #-Dado un numero, verifica si esta entre 10 y 20

# # numero_4= int(input("Ingresa el numero que te toco: "))

# # if 10 <= numero_4 <= 20:
# #     print(f"El numero esta entre 10 y 20 ({numero_4})")
# # else:
# #     print(f"El numero no esta entre 10 y 20 ({numero_4})")


# #----------------------------------------Ejercicio 5_condicionales-----------------------------------------#

# #-Dado tres numeros encuentre el mayor usando 

# numero_5= float(input("Ingresa el numero que te toco: "))


# numero_6= float(input("Ingresa el numero que te toco: "))


# numero_7= float(input("Ingresa el numero que te toco: "))

# if numero_5 > numero_6 >numero_7:
#     print(f"El numero {numero_5} es mayor que todos")

# elif numero_6 > numero_7 > numero_5:
#     print(f"El numero {numero_6} es mayor que todos")

# else:
#     print(f"El numero {numero_7} es el mayor que todos")

#----------------------------------------Ejercicio 6_condicionales-----------------------------------------#

#-Calcula el precio final con un 10% de descuento si el total es mayor a $100

# valor= float(input("Ingresa el precio de tu compra para cobrarte: "))

# procedimiento= valor * 0.10

# total= procedimiento + valor

# if valor > 100: 
#     print(f"su valor total es {total}")
# else:
#     print(f"su valor total es {valor}")



#----------------------------------------Ejercicio 7_condicionales-----------------------------------------#

#-Verifica si una persona puede votar (Mayor o igual a 18 años)


# edad= int(input("Ingresa tu edad actual: "))

# if edad >= 18:
#     print("Puede votar")
# else:
#     print("No puede votar")


#----------------------------------------Ejercicio 8_condicionales-----------------------------------------#

#-Dado el precio y tipo de cliente (VIP o normal) aplica el descuento del 20% solo a VIP

# print("""VALOR DE MESA:
#       VIP = 10000
#       normal = 5000""")

# print("""VALOR PRODUCTOS
#       CERVEZA = 5000
#       MANZANA = 2000
#       GASEOSA = 4000
#       ALMUERZO = 25000""")

# VIP_o_normal= int(input("Ingrese el valor que quiere pagar: "))

# producto_comprar= int(input("Ingrese el valor del producto que quiere comprar: "))

# descuento= producto_comprar * 0.20


# if VIP_o_normal == 10000:
#     print(f"""Usted es VIP y tienes un descuento del 20% del producto que quiere comprar que es {descuento}""")

# elif VIP_o_normal == 5000:
#     print(f"Usted es normal y no tiene descuento tiene que pagar esta cantidad por su producto {producto_comprar}")


#----------------------------------------Ejercicio 9_condicionales-----------------------------------------#

#-Determina si un numero es multiplo de 5 y de 3 al mismo tiempo

# multiplo= int(input("Ingresa un numero: "))


# if multiplo % 5 == 0 and multiplo % 3 == 0:
#     print("El numero es multiplo de 5 y de 3 al mismo tiempo")
# else:
#     print("El numero no es multiplo de 5 y de 3 al mismo tiempo")

#----------------------------------------Ejercicio 10_condicionales-----------------------------------------#

#dado un numero verifica si es divisible entre 2 numeros dados

# numero_20= int(input("Ingresa el número a verificar: "))


# divisor1 = int(input("Ingresa el primer divisor: "))


# divisor2 = int(input("Ingresa el segundo divisor: "))


# if numero_20 % divisor1 == 0 and numero_20 % divisor2 == 0:
#     print("El número es divisible entre los dos divisores")
# else:
#     print("El número no es divisible entre los dos divisores")














