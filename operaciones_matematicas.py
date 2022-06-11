#IMPORTAR UNA LIBRERÍA DE FUNCIONES MATEMÁTICAS
import math



# ENTRADA DE DATOS
numero_1 = float(input("Escribe el 1er número: "))
numero_2 = float(input("Escribe el 2do. número: "))





# PROCESOS (cálculos y/u Operaciones Matemáticas y Lógicas)
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1*numero_2
division= numero_1/numero_2
potencia1 = numero_1 ** numero_2
potencia2 = pow(numero_1 , numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2, 3)

raiz_cuadrada1 = math.sqrt(9)
raiz_cuadrada2 = pow(9, 1/2)
raiz_cubica = pow(9, 1/3)






# SALIDA DE DATOS
print("La suma =", round(suma, 2))
print("La suma =", str(round(suma , 2))) #CONCATENACIÓN (unión de textos)
#Convertir un tipo de dato en otro tipo de dato (CASTEO)
print(f"La suma ={round(suma,2)}")
print("La resta =", round((resta)))
print("La multiplicación =", str(round(multiplicacion, 2)))
print(f"La división = {round(division, 2)}")
print(f"La potencia 1 = {round(potencia1, 2)}")
print(f"La potencia 2 = {round(potencia2,2)}")
print(f"El cuadrado  = {round(cuadrado, 2)}")
print(f"El cubo = {round(cubo, 2)}")
print(f"La Raiz cuadrada 1 = {round(raiz_cuadrada1,2)}")
print(f"La Raiz cuadrada 2 = {round(raiz_cuadrada2, 2)}")
print(f"La raiz cubica = {round(raiz_cubica, 2)}")