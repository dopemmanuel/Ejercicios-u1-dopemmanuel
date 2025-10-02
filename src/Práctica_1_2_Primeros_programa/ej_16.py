""" Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), 
el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas."""

descuento = 0.60
pan = 3.49

vendidas = int(input("Cuantas barras se han vendido hoy? "))


price = 3.49 * (1 - descuento)

Total = price * vendidas

print(f"Actualmente el coste del pan recien hecho es de {pan}€,\nel pan que NO es de hoy le hacemos un descuento del {descuento}%\n y como has comprado {vendidas} cantidades del pan el total el precio total es de {round(Total, 2)}€.")