# #------------------------------------------------------------------EJERCICIO DICCIONARIOS 1-------------------------------------------------------------#


# #- PEDIR AL USUARIO TRES CALIFICACIONES Y ALMACENARLAS EN UNA LISTA Y CALCULAR EL PROMEDIO

# lista_pedidos= []


# pedido_1= int(input("Ingresa una calificacion: "))
# pedido_2= int(input("Ingresa otra calificacion: "))
# pedido_3= int(input("Ingresa ultima calificacion: "))


# lista_pedidos= [pedido_1, pedido_2, pedido_3]

# suma= pedido_1 + pedido_2 + pedido_3

# promedio= suma / 3

# print(f"Tu lista esta terminada {lista_pedidos} y el promedio de tus calificaciones es: {promedio} ")

# #------------------------------------------------------------------EJERCICIO DICCIONARIOS 1-------------------------------------------------------------#


# #-CREAR UN DICCIONARIO CON TRES PRODUCTOS Y SUS PRECIOS Y LUEGO PEDIR AL USUARIO QUE LE AUMENTE EL PORCENTAJE A CADA PRECIO

# diccionario_productos = {
#     "Tomate": 2500,
#     "Cebolla": 3600,
#     "Papa": 4000 
# }

# pedir_porcentaje = float(input("Agrega un porcentaje de aumento: "))

# diccionario_productos["Tomate"] += diccionario_productos["Tomate"] * (pedir_porcentaje / 100)
# diccionario_productos["Cebolla"] += diccionario_productos["Cebolla"] * (pedir_porcentaje / 100)
# diccionario_productos["Papa"] += diccionario_productos["Papa"] * (pedir_porcentaje / 100)

# print(diccionario_productos)

# #------------------------------------------------------------------EJERCICIO DICCIONARIOS 3--------------------------------------------------------------#


# #-GUARDAR EN UNA TUPLA LAS TEMPERATURAS EN GRADOS CELSIUS DE 5 DIAS Y CONVERTIR CADA UNA A FAHRENHEINT Y IMPRIMELAS

# temp_1= float(input("Ingresa una temperatura: "))

# temp_2= float(input("Ingresa otra temperatura: "))

# temp_3= float(input("Ingresa otra temperatura: "))

# temp_4= float(input("Ingresa otra temperatura: "))

# temp_5= float(input("Ingresa ultima temperatura: "))

# tupla_temp= (temp_1, temp_2, temp_3, temp_4, temp_5)

# fahre_1= temp_1 * 9/5 + 32
# fahre_2= temp_2 * 9/5 + 32
# fahre_3= temp_3 * 9/5 + 32
# fahre_4= temp_4 * 9/5 + 32
# fahre_5= temp_5 * 9/5 + 32

# print(f"el dia 1 la temperatura en fahrenheint es: {fahre_1} en el dia 2 es: {fahre_2} en el dia 2 es: {fahre_3} es el ")


# #------------------------------------------------------------------EJERCICIO DICCIONARIOS 4--------------------------------------------------------------#

# #- PEDIR AL USUARIO 5 EDADES ALMACENARLAS EN UNA LISTA Y MOSTRAR CUAL ES EL MAYOR EL MENOR Y EL PROMEDIO

# lista_edades=[]

# edades= int(input("Ingresa una edad: "))
# edades_1= int(input("Ingresa otra edad: "))
# edades_2= int(input("Ingresa otra edad: "))
# edades_3= int(input("Ingresa otra edad: "))
# edades_4= int(input("Ingresa ultima edad: "))

# lista_edades.append(edades)
# lista_edades.append(edades_1)
# lista_edades.append(edades_2)
# lista_edades.append(edades_3)
# lista_edades.append(edades_4)

# edad_mayor= max(lista_edades)
# edad_menor= min(lista_edades)

# promedio=(edades + edades_1 + edades_2 + edades_3 + edades_4 / 5)

# print(f"las edades en una lista compiladas son {lista_edades} y la edad mayor en esa lista es {edad_mayor} y la edad menor en esa lista es {edad_menor} y por ultimo el promedio de esa lista es: {promedio}")



#------------------------------------------------------------------EJERCICIO DICCIONARIOS 5--------------------------------------------------------------#

#- CREA UN DICCIONARIO CON TRES FRUTAS Y SUS PRECIOS POR KILO LUEGO PEDIR AL USUARIO LA CANTIDAD DE KILOS QUE QUIERE LLEVAR Y CALCULAR EL TOTAL A PAGAR

frutas = {"manzana": 3000, "banano": 2500, "pera": 2800}


kilo_1 = float(input("kilo de manzana: "))


kilo_2 = float(input("kilo de banano: "))


kilo_3 = float(input("kilo de pera: "))


total = kilo_1 * frutas["manzana"] + kilo_2 * frutas["banano"] + kilo_3 * frutas["pera"]


print(f"Total a pagar las frutas son: {total}")



#------------------------------------------------------------------EJERCICIO DICCIONARIOS 6--------------------------------------------------------------#


#-DEFINIR UNA TUPLA CON 5 NUMEROS MOSTRAR LA SUMA TOTAL DE LOS ELEMENTOS

tupla_numeros= (100, 200, 300, 400, 500)

print(f"La suma de la tupla es: ", sum(tupla_numeros)) 


#------------------------------------------------------------------EJERCICIO DICCIONARIOS 7--------------------------------------------------------------#

#-PIDE AL USUARIOQUE INGRESE NOMBRE, CANTIDAD Y PRECIO DE TRES PRODUCTOS Y ALMACENALOS COMO DICCIONARIO DENTRO DE UNA LISTA MUESTRA EL TOTAL DEL INVENTARIOS

producto_1 = input("¿Cuál es tu producto 1?: ")
cantidad = float(input("¿Cuánto del producto llevas (KG)?: "))
valor_1 = float(input("¿Cuánto vale tu producto?: "))

producto_2 = input("¿Cuál es tu producto 2?: ")
cantidad_2 = float(input("¿Cuánto del producto llevas (KG)?: "))
valor_2 = float(input("¿Cuánto vale tu producto?: "))

producto_3 = input("¿Cuál es tu producto 3?: ")
cantidad_3 = float(input("¿Cuánto del producto llevas (KG)?: "))
valor_3 = float(input("¿Cuánto vale tu producto?: "))

diccionario_frutas = {
    "producto_1": producto_1,
    "cantidad1": cantidad,
    "valor1": valor_1,

    "producto_2": producto_2,
    "cantidad2": cantidad_2,
    "valor2": valor_2,

    "producto_3": producto_3,
    "cantidad3": cantidad_3,
    "valor3": valor_3,
}

total_diccionario_valor = valor_1 + valor_2 + valor_3
total_diccionario_cantidad = cantidad + cantidad_2 + cantidad_3

print(f"""
Su inventario está terminado. Sus datos son:

Producto 1: {producto_1}
Cantidad: {cantidad} kg
Valor: ${valor_1}

Producto 2: {producto_2}
Cantidad: {cantidad_2} kg
Valor: ${valor_2}

Producto 3: {producto_3}
Cantidad: {cantidad_3} kg
Valor: ${valor_3}

TOTAL DE SU INVENTARIO (VALOR): ${total_diccionario_valor}
TOTAL DE SU INVENTARIO (CANTIDAD KG): {total_diccionario_cantidad} kg
""")


#------------------------------------------------------------------EJERCICIO DICCIONARIOS 8--------------------------------------------------------------#

#-CREAR UNA LISTA CON 5 PRECIOS PEDIR AL USUARIO UN DESCUENTO Y APLICARLO A TODOS LOS PRECIOS 

lista_precios= [5000,10000]















































