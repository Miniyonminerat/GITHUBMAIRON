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

precios = float(input("Precio 1: "))


precios_2 = float(input("Precio 2: "))


precios_3 = float(input("Precio 3: "))


precios_4 = float(input("Precio 4: "))


precios_5 = float(input("Precio 5: "))


precios = [precios, precios_2, precios_3, precios_4, precios_5]

descuento= float(input("Descuento: ")) 


descuento_1 = precios - (precios * descuento / 100)
descuento_2 = precios_2 - (precios_2 * descuento / 100)
descuento_3 = precios_3 - (precios_3 * descuento / 100)
descuento_4 = precios_4 - (precios_4 * descuento / 100)
descuento_5= precios_5 - (precios_5 * descuento / 100)


precios_descuento= [descuento_1, descuento_2, descuento_3, descuento_4, descuento_5]


print("Precios con descuento:", precios_descuento)



#------------------------------------------------------------------EJERCICIO DICCIONARIOS 9--------------------------------------------------------------#


#- CREAR UN TUPLA CON 5 NOTAS Y BUSCAR NOTA MAXIMA Y MINIMA

notas = (float(input("Ingresa primera nota: ")), float(input("Ingresa segunda nota: ")), float(input("Ingresa tercera nota: ")), float(input("Ingresa la cuarta nota:")))


print("Máxima:", max(notas), "Mínima:", min(notas))


#------------------------------------------------------------------EJERCICIO DICCIONARIOS 10--------------------------------------------------------------#

#-CONVERSION DE METROS 

conv = {"km": 1000, "m": 1, "cm": 0.01}


unidad = input("Unidad (km/m/cm): ")


valor = float(input("Cantidad: "))


print("En metros es:", valor * conv[unidad])

#------------------------------------------------------------------EJERCICIO DICCIONARIOS 11--------------------------------------------------------------#

#-PEDIR AL USUARIO 3 PRECIOS Y PASARLO A LISTAS LUEGO CREAR UNA LISTA CON EL PRECIO CON EL 19% DEL IVA (2 LISTAS)
precios_1_1 = float(input("Ingrese el primer precio: "))


precios_1_2 = float(input("Ingrese el segundo precio: "))


precios_1_3 = float(input("Ingrese el tercer precio: "))


precios_1_4 = [precios_1_1, precios_1_2, precios_1_3]


precio_iva_1 = precios_1_1 * 1.19


precio_iva_2 = precios_1_2 * 1.19


precio_iva_3 = precios_1_3 * 1.19


precios_con_iva = [precio_iva_1, precio_iva_2, precio_iva_3]


print("Precios con IVA del 19%:", precios_con_iva)






#------------------------------------------------------------------EJERCICIO DICCIONARIOS 12--------------------------------------------------------------#

#-PEDIR 2 NUMEROS HACER TUPLAS CON OPERACIONES Y IMPRIMIRLAS 

pedido_numero = float(input("Ingrese un numero: "))


pedido_numero_1 = float(input("Ingrese otro numero: "))


tupla_suma= (pedido_numero + pedido_numero_1)


tupla_resta= (pedido_numero - pedido_numero_1)


tupla_multiplicacion= (pedido_numero * pedido_numero_1)


tupla_divicion= (pedido_numero / pedido_numero_1)


print(f"""
      Sus operacion estan hechas los resultados son:
      SUMA: {tupla_suma}
      RESTA: {tupla_resta}
      MULTIPLICACION: {tupla_multiplicacion}
      DIVISION: {tupla_divicion}""")


#------------------------------------------------------------------EJERCICIO DICCIONARIOS 13--------------------------------------------------------------#

#-CREAR DICCIONARIO CON 3 ESTUDIANTES Y SUS NOTAS HALLAR EL PROMEDIO 
nombre1 = input("Nombre del estudiante 1: ")


nota1 = float(input("Nota de " + nombre1 + ": "))

nombre2 = input("Nombre del estudiante 2: ")


nota2 = float(input("Nota de " + nombre2 + ": "))

nombre3 = input("Nombre del estudiante 3: ")


nota3 = float(input("Nota de " + nombre3 + ": "))


estudiantes = {
    nombre1: nota1,
    nombre2: nota2,
    nombre3: nota3
}


promedio = (nota1 + nota2 + nota3) / 3


print("Notas registradas:", estudiantes)


print("Promedio general:", promedio)



#------------------------------------------------------------------EJERCICIO DICCIONARIOS 14--------------------------------------------------------------#



#-CALCULAR DICCIONARIO EL PRECIO 



salario1 = float(input("Ingrese el salario 1: "))


salario2 = float(input("Ingrese el salario 2: "))


salario3 = float(input("Ingrese el salario 3: "))


salario4 = float(input("Ingrese el salario 4: "))


salario5 = float(input("Ingrese el salario 5: "))


salarios = [salario1, salario2, salario3, salario4, salario5]


salario1_a = salario1 * 1.10


salario2_a = salario2 * 1.10


salario3_a = salario3 * 1.10


salario4_a = salario4 * 1.10


salario5_a = salario5 * 1.10


salarios_aumentados = [salario1_a, salario2_a, salario3_a, salario4_a, salario5_a]


print("Salarios originales:", salarios)
print("Salarios con aumento del 10%:", salarios_aumentados)







#------------------------------------------------------------------EJERCICIO DICCIONARIOS 15--------------------------------------------------------------#




product1 = input("Ingrese nombre del producto: ")


precio1 = float(input("Ingrese valor del producto: "))


product2 = input("Ingrese nombre del producto 2: ")


precio2 = float(input("Ingrese valor del producto 2: "))



pedir_aumento= float(input("Porcentaje de impuesto que quiere agregar: "))


lista=(precio1, precio2)

porcentaje_de_aumento_1= lista[0]*pedir_aumento / 100


porcentaje_de_aumento_2= lista[1]*pedir_aumento / 100


lista_2_impuesto= [porcentaje_de_aumento_1, porcentaje_de_aumento_2]

suma_1= precio1 + porcentaje_de_aumento_1


suma_2= precio2 + porcentaje_de_aumento_2



suma= precio1 + precio2 +  porcentaje_de_aumento_1 + porcentaje_de_aumento_2

print(f"""""
      La conversion de su impuesto esta completa y quedaria asi:
      PRECIO1 CON IMPUESTOS: {suma_1}
      PRECIO2 CON IMPUESTOS: {suma_2}
      SUMA DE PRECIOS CON IMPUESTOS: {suma}
      PRODUCTOS SON: {product1}, {product2}""")



#------------------------------------------------------------------EJERCICIO DICCIONARIOS 16--------------------------------------------------------------#

#-PEDIR AL USUARIO 5 EDADES METERLAS EN UNA LISTA Y MIRAR CUALES SON MAYORES DE EDAD Y CUALES SON MENORES DE EDAD


edad_1_2= int(input("Ingrese edad 1: "))


edad_1_3= int(input("Ingrese edad 2: "))


edad_1_4= int(input("Ingrese edad 3: "))


edad_1_5= int(input("Ingrese edad 4: "))


edad_1_6= int(input("Ingrese edad 5: "))


lista_de_edades= [edad_1_2, edad_1_3, edad_1_4, edad_1_5, edad_1_6]


mayores= (edad_1_2 >= 18) + (edad_1_3 >= 18) + (edad_1_4 >=18) + (edad_1_5 >= 18) + (edad_1_6 >= 18)

menores = 5 - mayores


print(f"las personas mayores de edad son {mayores} y las que son menores de edad son {menores}")


#------------------------------------------------------------------EJERCICIO DICCIONARIOS 17--------------------------------------------------------------#

#-CONVERSION DE MONEDA PEDIR AL USUARIO QUE INGRESE LA CONVERSION O CANTIDAD DE DOLARES QUE QUIERA CONVERTIR HACE LA OPERACION CON LA TASACION POR DOLAR QUE DA EN CADA UNO EJM PESOS 1 DOLAR ES 3900 Y SI MULTIPLICA

hallar_dinero_usd= float(input("Ingresa los dolares que quieres pasar a otra moneda: "))

euros= hallar_dinero_usd * 0.85


pesos= hallar_dinero_usd * 3900


yenes= hallar_dinero_usd * 110

print(f"""
      En euros quedaria en: {euros}
      En pesos quedaria en: {pesos}
      En yenes quedaria en: {yenes}  """)



#------------------------------------------------------------------EJERCICIO DICCIONARIOS 18--------------------------------------------------------------#

#- DICCIONARIO DE VENTA


producto_venta_1= input("Ingrese el nombre del producto 1 vendido: ")


valor_venta_1= float(input("Ingrese el valor del producto_1 vendido: "))


cantidad_venta_1= float(input("Ingrese cantidad llevada (KG): "))



producto_venta_2= input("Ingrese el nombre del producto_2 vendido: ")


valor_venta_2= float(input("Ingrese el valor del producto_2 vendido: "))


cantidad_venta_2= float(input("Ingrese cantidad llevada (KG): "))



producto_venta_3= input("Ingrese el nombre del producto_3 vendido: ")


valor_venta_3= float(input("Ingrese el valor del producto_3 vendido: "))


cantidad_venta_3= float(input("Ingrese cantidad llevada (KG): "))



total_valor_1= valor_venta_1 * cantidad_venta_1

total_valor_2= valor_venta_2 * cantidad_venta_2

total_valor_3= valor_venta_3 * cantidad_venta_3



diccionario_ventas= {

        producto_venta_1: total_valor_1,

        producto_venta_2: total_valor_2,

        producto_venta_3: total_valor_3

}


print(f"""
      El diccionario de ventas esta terminado esta es las ventas que se hicieron en el mes: 
      
      {diccionario_ventas}""")


#------------------------------------------------------------------EJERCICIO DICCIONARIOS 19--------------------------------------------------------------#

#-TEMPERATURAS RE DIFICILES Y LARGOS :V



temperatura_1_1= float(input("Ingrese primera temperatura"))


temperatura_1_2= float(input("Ingrese segunda temperatura: "))


temperatura_1_3= float(input("Ingrese tercera temperatura: "))


temperatura_1_4= float(input("Ingrese cuarta temperatura: "))


temperatura_1_5= float(input("Ingrese quinta temperatura: "))


temperatura_1_6= float(input("Ingrese sexta temperatura: "))


temperatura_1_7= float(input("Ingrese septima temperatura: "))


temperatura_1_8= float(input("Ingrese octava temperatura: "))


temperatura_1_9= float(input("Ingrese novena temperatura: "))


temperatura_1_10= float(input("Ingrese decima temperatura: "))


lista_temperaturas= [temperatura_1_1, temperatura_1_2, temperatura_1_3, temperatura_1_4, temperatura_1_5, temperatura_1_6, temperatura_1_7, temperatura_1_8, temperatura_1_9, temperatura_1_10]




mayores_30 = [
    temperatura_1_1 * (temperatura_1_1 > 30), temperatura_1_2 * (temperatura_1_2 > 30),


    temperatura_1_3 * (temperatura_1_3 > 30), temperatura_1_4 * (temperatura_1_4 > 30),


    temperatura_1_5 * (temperatura_1_5 > 30), temperatura_1_6 * (temperatura_1_6 > 30),


    temperatura_1_7 * (temperatura_1_7 > 30), temperatura_1_8 * (temperatura_1_8 > 30),


    temperatura_1_9 * (temperatura_1_9 > 30), temperatura_1_10 * (temperatura_1_10 > 30)
]


menores_10 = [
    temperatura_1_1 * (temperatura_1_1 < 10), temperatura_1_2 * (temperatura_1_2 < 10),


    temperatura_1_3 * (temperatura_1_3 < 10), temperatura_1_4 * (temperatura_1_4 < 10),


    temperatura_1_5 * (temperatura_1_5 < 10), temperatura_1_6 * (temperatura_1_6 < 10),


    temperatura_1_7 * (temperatura_1_7 < 10), temperatura_1_8 * (temperatura_1_8 < 10),


    temperatura_1_9 * (temperatura_1_9 < 10), temperatura_1_10 * (temperatura_1_10 < 10)
]


print("Temperaturas mayores a 30:")


print(temperatura_1_1 * (temperatura_1_1 > 30))


print(temperatura_1_2 * (temperatura_1_2 > 30))


print(temperatura_1_3 * (temperatura_1_3 > 30))


print(temperatura_1_4 * (temperatura_1_4 > 30))


print(temperatura_1_5 * (temperatura_1_5 > 30))


print(temperatura_1_6 * (temperatura_1_6 > 30))


print(temperatura_1_7 * (temperatura_1_7 > 30))


print(temperatura_1_8 * (temperatura_1_8 > 30))


print(temperatura_1_9 * (temperatura_1_9 > 30))


print(temperatura_1_10 * (temperatura_1_10 > 30))



print("Temperaturas menores a 10:")


print(temperatura_1_1 * (temperatura_1_1 < 10))


print(temperatura_1_2 * (temperatura_1_2 < 10))


print(temperatura_1_3 * (temperatura_1_3 < 10))


print(temperatura_1_4 * (temperatura_1_4 < 10))


print(temperatura_1_5 * (temperatura_1_5 < 10))


print(temperatura_1_6 * (temperatura_1_6 < 10))


print(temperatura_1_7 * (temperatura_1_7 < 10))


print(temperatura_1_8 * (temperatura_1_8 < 10))


print(temperatura_1_9 * (temperatura_1_9 < 10))





#------------------------------------------------------------------EJERCICIO DICCIONARIOS 20--------------------------------------------------------------#


#-ORGANIZAR EN UNA LISTA DE MENOR A MAYOR 




valor_precio1 = float(input("Ingrese el precio 1: "))


valor_precio2 = float(input("Ingrese el precio 2: "))


valor_precio3 = float(input("Ingrese el precio 3: "))


valor_precio4 = float(input("Ingrese el precio 4: "))


valor_precio5 = float(input("Ingrese el precio 5: "))



LISTA_PRECIOS_5= [valor_precio1, valor_precio2, valor_precio3, valor_precio4, valor_precio5]


eliminar_precios= float(input("¿Que precio quiere usted eliminar?: "))

LISTA_PRECIOS_5.remove(eliminar_precios)


nuevo_precios= float(input("¿Que valor quiere agregar usted?: "))

LISTA_PRECIOS_5.append(nuevo_precios)

LISTA_PRECIOS_5.sort()


print(f"""La lista esta completada y ordenada de menor a mayor quedo asi: 
      
      {LISTA_PRECIOS_5}""")





