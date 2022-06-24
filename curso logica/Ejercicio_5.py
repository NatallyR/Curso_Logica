# LIBRERIA
import math 

# ENTRADA DE DATOS
valor_a = float(input("Escriba el valor de a: "))
valor_b = float(input("Escriba el valor de b: "))
valor_c = float(input("Escriba el valor de c: "))

# PROCESOS
raiz_1 = (-valor_b - (math.sqrt((valor_b ** 2)- (4* valor_a * valor_c)))) / (2 * valor_a)
raiz_2 = (-valor_b + (math.sqrt((valor_b ** 2) - (4 * valor_a * valor_c)))) / (2 * valor_a)

# SALIDA DE DATOS
print(f"x1 = {round(raiz_1, 2)}")
print(f"x2 = {round(raiz_2, 2)}")