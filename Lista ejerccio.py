#-Crear una lista vacia llamada frutas luego pedir al usuario que escriba 3 frutas diferentes y usa .append() para agregarlas ala lista

#-----------------------------------------------------------------------------Ejercicio 1-----------------------------------------------------------------------------#

# frutas= []
# print(frutas)

# frut_1= input("Ingresa una fruta ")
# frut_2= input("Ingresa otra fruta ")
# frut_3= input("Ingresa ultima fruta ")


# frutas.append(frut_1)
# frutas.append(frut_2)
# frutas.append(frut_3)
# print(frutas)

#-----------------------------------------------------------------------------Ejercicio 2-----------------------------------------------------------------------------#



# lista_edades= []

# print(lista_edades)

# edades= int(input("Ingrese una edad"))
# edades_2= int(input("Ingrese otra edad"))

# lista_edades.append(edades)
# lista_edades.append(edades_2)

# print(lista_edades)


#-----------------------------------------------------------------------------Ejercicio 3-----------------------------------------------------------------------------#


# notas_deci= float(input("Ingresa una nota con decimal"))
# notas_deci_2= float(input("Ingresa otra nota con decimal"))

# listas_notas= []

# listas_notas.append(notas_deci)
# listas_notas.append(notas_deci_2)

# print(listas_notas)

#-----------------------------------------------------------------------------Ejercicio 4-----------------------------------------------------------------------------#

# lista_productos= []

# nombre_producto= input("Ingresa nombre de producto 1 ")
# nombre_producto_2= input("Ingresa nombre de producto 2 ")
# nombre_producto_3= input("Ingresa nombre de producto 3")

# lista_productos.append(nombre_producto)
# lista_productos.append(nombre_producto_2)
# lista_productos.append(nombre_producto_3)

# print(lista_productos)


#-----------------------------------------------------------------------------Ejercicio 5-----------------------------------------------------------------------------#



# valor_producto= float(input("Ingresa el valor de el primer producto: "))
# valor_producto_2= float(input("Ingresa el valor de el segundo producto: "))
# valor_producto_3= float(input("Ingrese el valor de el tercer producto :"))


# lista_precios= [valor_producto,valor_producto_2,valor_producto_3,]
# print(lista_precios)

# operacion= valor_producto + valor_producto_2 + valor_producto_3
# print(operacion)

#-----------------------------------------------------------------------------Ejercicio 6-----------------------------------------------------------------------------#


# numero_1= int(input("Ingresa un numero: "))
# numero_2= int(input("Ingresa otro numero: "))
# numero_3= int(input("Ingresa otro numero: "))
# numero_4=int (input("Ingresa ultimo numero: "))

# lista_numeros= []

# lista_numeros.append(numero_1)
# lista_numeros.append(numero_2)
# lista_numeros.append(numero_3)
# lista_numeros.append(numero_4)

# print("El numero mayor es :", max(lista_numeros))
# print("El numero menor es :", min(lista_numeros))

#-----------------------------------------------------------------------------Ejercicio 7-----------------------------------------------------------------------------#


# lista_completed = [] 

# nombre_completo = input("Ingresa un nombre completo: ")
# nombre_completo_2 = input("Ingresa otro nombre completo: ")


# lista_completed.append(nombre_completo)
# lista_completed.append(nombre_completo_2)

# print(f"Hola, {nombre_completo} y {nombre_completo_2} ¿como estan?")
#-----------------------------------------------------------------------------Ejercicio8-----------------------------------------------------------------------------#



# lista_temperaturas = []

# temperaturas = int(float(input("Ingrese la temperatura 1: ")))
# temperaturas_2 = int(float(input("Ingrese otra temperatura 2: ")))

# lista_temperaturas.append(temperaturas)
# lista_temperaturas.append(temperaturas_2)

# fahrenheit = temperaturas * 9/5

# resultado_fahrenheit= fahrenheit + 32

# fahrenheit_2 = temperaturas_2 * 9/5

# resultado_fahrenheit_2= fahrenheit_2 + 32

# print(f"Los grados dados son {temperaturas} y {temperaturas_2} y si los pasamos a fahrenheit son {resultado_fahrenheit} y {resultado_fahrenheit_2} ")


#-----------------------------------------------------------------------------Ejemplo remove-----------------------------------------------------------------------------#


# frutas = ["manzana", "banana", "naranja", "banana"]
# frutas.remove("banana")

# print(frutas)





# #------------------------------------------------------------------Ejercicio clase .append------------------------------------------------------------#

# #--------- primero -------#

# lista_vacia= []

# lista_vacia.append(7)

# print(lista_vacia)


# #--------- segundo -------#

# lista_nombres= ["Ana, " "Luis "]

# lista_nombres.append("Carlos")

# print(lista_nombres)


# #------------------------------------------------------------------Ejercicio clase .insert------------------------------------------------------------#


# #--------- primero -------#

# lista_numeros= [1, 2, 3,]


# lista_numeros.insert(0,99)

# print(lista_numeros)


# #--------- segundo -------#

# lista_colores= ["azul," " verde"]



# lista_colores.insert(0,"rojo")


# print(lista_colores)



# #------------------------------------------------------------------Ejercicio clase .extend(iterable)------------------------------------------------------------#

# #--------- primero -------#

# lista_numeros_1= [4, 5, 6]

# lista_numeros_1.extend([1, 2, 3])

# print(lista_numeros_1)


# #--------- segundo -------#

# lista_letras= ["a", "b",]

# lista_letras.extend(["ok"])

# print(lista_letras)




# #------------------------------------------------------------------Ejercicio clase .remove-------------------------------------------------------------------#

# #--------- primero -------#

# lista_frutas= ["manzana", "uva", "pera"]

# lista_frutas.remove("uva")

# print(lista_frutas)

# #--------- segundo -------#

# lista_numeros_2= [1, 2, 3, 2]

# lista_numeros_2.remove(2)

# print(lista_numeros_2)


# #------------------------------------------------------------------Ejercicio clase .pop-------------------------------------------------------------------#

# #--------- primero -------#


# lista_numeros_3= [1, 2, 3, 4]

# valor= lista_numeros_3.pop()

# print(valor)

# print(lista_numeros_3)

# #--------- segundo -------#


# lista_letras_1= ["uno", "dos", "tres"]

# valor_1= lista_letras_1.pop(0)


# print(lista_letras_1)

# #------------------------------------------------------------------Ejercicio clase .clear-------------------------------------------------------------------#


# #--------- primera -------#


# lista_numeros_4= [1, 2, 3]

# lista_numeros_4.clear()

# print(lista_numeros_4)


# #--------- segundo -------#

# lista_elementos= ["pepe", "nemo", 1, 98, "colombia"]

# lista_elementos.clear()

# print(lista_elementos)


# #------------------------------------------------------------------Ejercicio clase .index-------------------------------------------------------------------#



# #--------- primero -------#

# lista_frutas_1= ["manzana", "pera", "uva"]

# lista_frutas_1.index("pera")

# print(lista_frutas_1.index("pera"))

# #--------- segundo -------#

# lista_dado_numeros= [4, 5, 6, 7]

# lista_dado_numeros.index(6)


# print(lista_dado_numeros.index(6))


# #------------------------------------------------------------------Ejercicio clase .count------------------------------------------------------------------#


# #--------- primero -------#

# lista_aparece= [3, 1, 3, 5, 3]

# lista_aparece.count(3)

# print(lista_aparece.count(3))


# #--------- segundo -------#



# lista_letras_2= ["a", "b", "a", "c", "a"]

# lista_letras_2.count("a")

# print(lista_letras_2.count("a"))

# #------------------------------------------------------------------Ejercicio clase .sort------------------------------------------------------------------#


# #--------- primero -------#

# lista_numeros_5= [5, 1, 4, 2, 3]

# lista_numeros_5.sort()

# print(lista_numeros_5)

# #--------- segundo -------#


# lista_letras_3= ["z", "a", "m", "b"]

# lista_letras_3.sort()

# print(lista_letras_3)

# #------------------------------------------------------------------Ejercicio clase .reverse------------------------------------------------------------------#

# #--------- primero -------#

# lista_invertida= [1, 2, 3, 4]

# lista_invertida.reverse()

# print(lista_invertida)

# #--------- segundo -------#

# lista_invertida_1= ["inicio", "medio", "fin"]

# lista_invertida_1.reverse()

# print(lista_invertida_1)


# #------------------------------------------------------------------Ejercicio clase .copy--------------------------------------------------------------------#



# #--------- primero -------#


# lista_copiar= [1, 2, 3]

# nueva_lista= lista_copiar.copy()

# print(lista_copiar) # resultado [1, 2, 3]


# print(nueva_lista) # resultado [1, 2, 3]


# #--------- segundo -------#


# lista_copiar_1= ["a", "b", "c"]

# nueva_lista_1= lista_copiar_1.copy()

# nueva_lista_1.append("d")

# print(lista_copiar_1)
# print(nueva_lista_1)
















