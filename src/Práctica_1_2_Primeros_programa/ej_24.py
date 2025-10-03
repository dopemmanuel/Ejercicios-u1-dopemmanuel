""" Escribir un programa que pregunte por consola el precio de un producto en euros con dos 
decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""

euros = float(input("Introduce cuantos € vale el producto: "))

int_a_str = str(euros)

entera, decimal = int_a_str.split(".")
print(f"{entera} euros con {decimal} centimos.")