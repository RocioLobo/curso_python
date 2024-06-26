# crear una funccion que reciba por argumentos n numeros y retorne una lista con los numeros pares


def num_pares(*args):
    pares=[]
    for n in args:
        if n%2==0:
            pares.append(n)
        return pares
print(num_pares(8,4,16,4,5,4))   


#por compresion
#return [n for n in args if n%2==0]
print(num_pares(8,5,4,7,9,25,4,7,12))

#crear tres funciones para los siguientes casos 
# calcular el numero menor
# calcular el numero mayor
# calcular la suma de todos los numeros
# se le pasara por argumento n numeros

def min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
    
def max(*args):
    mayor=args[0]
    for n in args:
        if n<mayor:
            mayor=n
    return mayor

def sum(*args):
    suma=0
    for n in args:
        suma+=n

    return suma

    


valores=[4,7,8,5,2,1]
print(Min(*valores))
print(Max(*valores))
print(Sum(*valores))


# (tarea)
# crear una lista de alumnos con los siguientes campos
# nombre ,apellido, edad, celular, email
# 1. actualizar los registro con un campo mas todos tendran el campo de programa de estudios de enfermeria
# 2. buscar el segundo registro y actualizar su edad de 50 años.




