#1.Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
#Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
#Multiplica el numero_usuario por 9 en sí mismo
#Multiplica el numero_magico por el numero_usuario en sí mismo
#Finalmente muestra el valor final del numero_magico por pantalla
numero_smagico=12345679
numero_usuario=input("Ingresa un Numero del 1 al 9: ")
numero_usuario=int(numero_usuario)
numero_usuario= numero_usuario * 9
multiplicacion=numero_usuario *numero_magico
print(f"numero magico:{multiplicacion} ")



