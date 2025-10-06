"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""

veces = 3
nom1 = input("Introduce tu nombre o lo que sea: ")

for i in range(0,veces):
    print(f"{nom1.upper()}\n{nom1.lower()}")
