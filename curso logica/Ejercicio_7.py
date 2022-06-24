# ENTRADA
nivel_de_agua = float (input("Introduce el nivel de agua: "))

#PROCESOS
if (nivel_de_agua > 6):
    print ("Desbordamiento de agua en cisterna")
if (nivel_de_agua == 6):
    print ("Apagar Bomba")
if (nivel_de_agua >= 4 and nivel_de_agua <= 5.99):
    print ("Desacelerar Bomba")
if (nivel_de_agua >= 2 and nivel_de_agua <= 3.99):
    print ("Bomba Trabajando")
if (nivel_de_agua >= 0.1 and nivel_de_agua <= 1.99):
    print ("Acelerar bomba de agua")
if (nivel_de_agua == 0):
    print ("Encender Bomba de agua")
if (nivel_de_agua < 0):
    print ("Fuga en cisterna")
#SALIDAS
