#ENTRADA DE DATOS
calificacion_1 = float (input("Escriba la 1er calificación: "))
calificacion_2 = float (input("Escriba la 2da. calificación: "))
calificacion_3 = float (input("Escriba la 3ra. calificación: "))

#PROCESOS
suma = calificacion_1 + calificacion_2 + calificacion_3
promedio = suma / 3

#SALIDA DE DATOS
print(f"El promedio  = {round(promedio, 2)}")
if (promedio >= 6.1 and promedio<= 10.0):
    print ("APROBADO")
if (promedio == 6 ):
    print ("PANSASO")
if (promedio >= 0 and promedio <= 5.99):
    print ("REPROBADO")
if (promedio <0 or promedio >10):
    print ("ERROR EN PROMEDIO")