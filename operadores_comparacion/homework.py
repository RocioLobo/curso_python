#1.Utilizando operadores de comparación, determina si un numero introducido por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10
numero_usuario:str=input('ingrese por favor un numero: ')
longitud=len(numero_usuario)
comparar=longitud >= 3 and longitud < 10
print(comparar)


#2.Comparar dos edades ingresadas por el usuario y determinar si son iguales o diferentes.
edad1=int(input("ingrese primer numero de edad por favor:"))
edad2=int(input("ingrese segundo numero   de edad por favor:"))
if edad1==edad2:
	print("son iguales  ")
elif (edad1<edad2):
	print("son diferentes  ")