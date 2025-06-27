#-CREAR DICCIONARIO DE AUTO


auto = {

"marca": "Ford",
"modelo": "Mustang",
"año": "2022",
"motor": "V8",
"color": "rojo",

}

print(auto)


#-IMPRIMIR EL MODELO DEL DICCIONARIO AUTO



print(auto["modelo"]) 



#-MODIFICAR VALORES DE LOS DICCIONARIOS 



auto["año"]= 2045



#-IMPRIMIR VALOR MODIFICADO 



print(auto["año"]) #- RESULTADO ES 2045



#-AÑADIR NUEVA KEY O LLAVE AL DICCIONARIO



auto["reparado"]= "NO" #- DEBERIA AÑADIR UNA LLAVE: "reparado": "NO"



#-IMPRIMIR EL DICCIONARIO Y VER LA LLAVE AGREGADA



print(auto)

#-ELIMINAR ELEMENTOS DEL DICCIONARIO USANDO del



del auto["modelo"]


#-ELIMINAR ELEMNTOS DEL DICCIONARIO USANDO .pop()



auto.pop("marca")



#-IMPRIMIR RESULTADO FINAL DE LA ELIMINACIO DEL ELEMENTO

print(auto)
















