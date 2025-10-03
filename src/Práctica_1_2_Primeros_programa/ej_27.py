""" Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades 
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos 
enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

producto = input("Me dices el nombre del producto? ")
precio = float(input("Me dices el precio unitario? "))
unidades = int(input("Cuantas unidades te vas a llevar? "))


Total = precio * unidades

print(f"{producto} cuesta {precio:09.2f}€, por unidad que son {unidades:03d} serian unos {Total:011.2f}€")