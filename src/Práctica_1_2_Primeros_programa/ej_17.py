"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

nombre = input("Ingresa tu nombrre de usuario: ")
contadas = int(input("Ingresa el numero de veces que quieres que apareza tu nombre: "))

for i in range(0,contadas):
    print(nombre)
