# tipos de datos estructurados(TDA - Tipos de datos abstractos) tenemos como la lista.
#lista - sus valores o elementos se pueden  actualizar, eliminar
lista=["abel",20,5.2,.5,false,["texto",.2]]
```pyton
#tupla- sus valores o elementos no pueden ser modificados o eliminados.
tupla=("abel",20,5.2,False,[])
#diccionarios se e conoce como objetos
# los diccionarios almacenan los datos con clave y valor y te muestran el valor al imprimir 
diccionario={"nombre":"antonio","edad":15,"sexo":False}
```
-[!TIP]
-**obsercvacion:** que los tipos de datos estructurados pueden alamacenar en su interior otros tipos de datos estructurados

```pyton
lista_alumnos=[
    {
        "nombre
    }
]

## METODOS
###1. convertir texto a lista
```pyton

#METODO LIST

te canbia los textos cortos.
texto="hola"2
list(texto)
#["h","o","l","a"]

# METODO SPLIT

son para textos largos , trosea texto  en una lista atravez de un limitador y lo separa como comas, puntos eslash etc.
texto="hola como estan alumnitos lindo"
texto.split(",")

texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split(" ")
print(nuevo_texto)


#METODO JOIN
#con texto largo
texto_largo="este es un texto largo chiquititas y chiquititos"
nuevo_texto=texto_largo.split(" ")
print(",".join(nuevo_texto))

### 2.Agregar elementos al final de una lista
```pyton

# METODO APPEND - es un metodo que me permite agregar elementos al final de una lista
lista=["hola"]
lista.append("mundo")
print(lista)
#["Hola","mundo"]

#METODO INSERT -es el metodo que me permite agregar elementos en cualquier ubicacion de li lista
lista_nombres=["edith","ruth","LUZ"]
lista_nombres.insert(0,"antony")

### 3.Eliminar elementos de una lista
```pyton

#METODO POP - es el metodo que elimina el ultimo elemento de una lista es el contrario de append.

lista_nombres=["edith","ruth","LUZ"]
lista_nombres.pop() eliminara el ultimo nombre

#primera manera -METODO REMOVE -este metodo elimina el por el nombre el elemento que coincida dentro de mi lista.

lista_nombres=["edith","ruth","LUZ"]
lista_nombres.remove(edith) eliminara el nombre que coincida y escojas remove lo ase

#segunda opcion -METODO POP- al pasarle por parametro u n indice este lo eliminara de la lista.

lista_nombres=["edith","ruth","LUZ"]
lista_nombres.pop(0) eliminara por indice como 0 1 2 depende donde corresponde si no pones el indice automaticamente eliminara el ultimo.


### 4. Buscar un elemento en una lista

lista_nombres=["edith","ruth","LUZ"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])  te mostrara el indice del nombre seleccionado.

pertenencia="edith" in lista_nombres #true False

```





