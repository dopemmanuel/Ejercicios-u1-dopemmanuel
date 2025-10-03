""" Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y 
muestre por pantalla cada uno de los productos en una línea distinta."""

Prod_Cesta = input("Ingrese los productos de su cesta de compras: ").split(",")

print("Productos en la cesta de la compra: ")

for producto in Prod_Cesta:
    print(f"-  {producto}")
