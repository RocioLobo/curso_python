#LISTA
lista=["abel","antony","2miguel"]
print(lista[1])

#DICCIONARIO
diccionario=diccionario={"nombre":"antonio","edad":15,"sexo":False}
print(diccionario["nombre"])


#SPLIT
texto="hola"
lista_texto=list(texto)
print(lista_texto)

texto="hola"
lista_texto=list(texto)
lista2=[e for e in texto]
print(lista2)

#LIST
texto_largo="hola como estan bienvenidos al salon"
nueva_lista=texto_largo.split(" ")
print(nueva_lista)


#te mostrara solo del 16 para adelante ejm: bienvenidos al salon.
texto_largo="hola como estan bienvenidos al salon"
nuevo_texto=texto_largo[16:]
nueva_lista=nuevo_texto.split(" ")
print(nueva_lista)

#SPLIT
texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split(" ")
print(nuevo_texto)


#JOIN al poner las comillas te separa si pones junto las comillas el texto saldra junto.y si pones un espacio el texto saldra con espacio.
texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split("_")
print(" ".join(nuevo_texto))

#con texto largo : cuando quieres separar ya sea con comas puntos o espacios.
texto_largo="este es un texto largo chiquititas y chiquititos"
nuevo_texto=texto_largo.split(" ")
print(",".join(nuevo_texto)) 
