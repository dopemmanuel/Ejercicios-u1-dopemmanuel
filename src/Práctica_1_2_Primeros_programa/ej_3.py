"""
Suponiendo que se han ejecutado las siguientes sentencias de asignación:

ancho = 17
alto = 12.0
para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:

1. ancho / 2 
2. ancho // 2
3. alto / 3
4. 1 + 2 * 5

"""

ancho = 17
alto = 12.0


choose = int(input("Seleciona una de estas operaciones(1-4): "))


if choose == 1 :
    opcion1 = ancho / 2
    print(f"{opcion1} es un float")

elif choose == 2 :
    opcion2 = ancho // 2
    print(f"La opcion {opcion2} es un int ")

elif choose == 3:
    opcion3 = alto / 3
    print(f"{opcion3} eso es un float")

elif choose == 4:
    opcion4 = 1 + 2 * 5
    print(f"{opcion4} es un int")
else:
    print("() -_-)_Esa opcion no es valida_(-_-()")
