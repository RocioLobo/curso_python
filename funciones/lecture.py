# return devuelve valores que podre hacer uso
# crear una funcion que retorne el numero 10 y muestra por terminal si es par
# siempre que el valor que retorne mi funcion se utilize en mas sentencias u operaciones hacer uso de return
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar")


# print solo muestra por terminal


# return cuando queremos que muestra funcion devuelva o retporne un tipo de dato o un tipo de dato estructurado.


#cear una funcion que me muestre el producto de dos numeros
def procducto(a,b):
    return a*b


#crear una funcion que me retorne una lista de tres  numeros

def lista_numeros():
    return [3,2,6]

# print usaremos cada vez que nuestra funcion retorne un mensaje
# crear una funcion que por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre

def mensaje(nombre):
    print(f"hola,{nombre},bienvenido al chongo")


# crear una funcion que reciba por parametro una lista de numeros y me devuelva el numero menor ,mostrar por terminal el valor retornado por la funcion.
lista=[4,3,6,78,7]
def Min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
print(Min(lista))

# crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar un diccionario con los datos, luego mostrar por terminal el valor de retorno de mi funcion.

nombre="abel"
edad=19
def persona(nom,edad):
    return{
        "nombre":nom,
        "edad":edad
    }
print(persona(nombre,edad))

#1. desempaquetado/Empaquetado de argumentos(tarea)
# vamos a implementar una función para sumar un número variable de valores.
# EMPAQUETANDO
#vamos a hacer uso del * para empaquetar los argumentos posicionales:
## EMPAQUETANDO

def _sum(*values):
    print(f'{values=}')
    result = 0
    for value in values:  # values es una tupla
        result += value
    return result
_sum(4, 3, 2, 1)
values=(4, 3, 2, 1)
10

# DESENPAQUETANDO: _sum(4, 3, 2, 1)
_sum(*values)
values=(4, 3, 2, 1)
# 10

# FUNCIONES INTERNAS EN PYTON.

# en el que extraemos las palabras de un texto que contienen todas las vocales, haciendo uso de una función interior que nos devuelve el número de vocales distintas que tiene cada palabra:

def get_words_with_all_vowels(text: str) -> list[str]:
    VOWELS = 'aeiou'
    def get_unique_vowels(word: str) -> set[str]:
        return set(c for c in word if c in VOWELS)
    result = []
    for word in text.split():
        if len(get_unique_vowels(word)) == len(VOWELS):
            result.append(word)
    return result

get_words_with_all_vowels('La euforia de ver el riachuelo fue inmensa')
['euforia', 'riachuelo']
