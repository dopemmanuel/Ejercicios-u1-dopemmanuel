"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguiente: 
"la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por 
el usuario, y c y r son el cociente y el resto de la división entera respectivamente: """


n = int(input("Ingrese el primer numero: ")) 
m = int(input("Ingrese el segundo numero entero: "))

c = n // m
r = n % m

print(f"La división de {n} entre {m} da un cociente {c} y un resto {r}.")
