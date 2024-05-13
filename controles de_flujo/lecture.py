# ejemplo de if
if true:
    print("verdad")

#ejemplo de for
#imprimir los numeros pares
#entre 1 -20
for n in range(1,21):
    if n%2==0:
        print(n)

#crear un programa que me imprima las 5vocales
vocales:str="aeiou"
for n in range (0,5):
    print(vocales[n])

# crear un programa que me muestre los 8 primeros numeros pares.
contador=0
for n in range (1,17):
    if n%2==0:
        contador+=1
        print(f"{n} es el numero{contador} ")

# crear un programa que pida al usuario escribir una oracion
# y mostrar por terminal la cantidad de vocales a que
# tiene esa oracion
# OJO:SOLO LAS "a" MINUSCULA

oracion:str=input("escribe una oracion: ")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]=="a":
        contador=contador+1
        #contador+=1
print(f"la cantidad de letras a que  tengo e es {contador}")

# cear un programa que me comente la cantaidad de comas y me muestre
#sus indices.
#OJO. tiene que pedir al usuario
cantidad:str=input()








# ejemplos de if - else primer ejemplo de if estructurado:

edad:int=int(input("escribe tu edad"))
if edad>18:
    print("eres mayor")
else:
    print("eres menor de edad")



