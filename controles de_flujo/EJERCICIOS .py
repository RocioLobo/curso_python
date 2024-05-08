1.#escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad1=int(input("ingresa primera edad:"))
if edad1>=18:
     print(" es mayor de edad")
else:
    print("menor de edad")


2.#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas.

contraseña = "rociolobo"
contraseña = input("Introduce la contraseña: ")
if contraseña == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")




3.#Escribir un programa  que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas.
numero=int(input("introduce un numero entero positivo:"))
if numero<0:
     print("no se permiten numeros negativos")
else:
     for i in range(numero,-1,-1):
        print(i, end=",")




