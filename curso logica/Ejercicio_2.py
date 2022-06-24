# ENTRADA DE DATOS
from cmath import pi


radio = float(input ("Escriba el radio: "))
PI = 3.1416

# PROCESOS
perimetro = 2 * radio * PI
area = PI * (radio ** 2)

# SALIDA DE DATOS
print(f"El perimetro  = {round(perimetro, 2)}")
print(f"El área  = {round(area, 2)}")
