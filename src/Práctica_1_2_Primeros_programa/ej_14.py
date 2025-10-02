"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que 
deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos 
y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

payasos = 112
muniecas = 75


cantidad1 = int(input("Cuantos payasos de jugete quieres comprar? "))
cantidad2 = int(input("Cuantas muñecas quieres comprar? "))

peso = (cantidad1 * payasos) + (cantidad2 * muniecas)

print(f"El peso total de su paquete con la cantidad de muñecas: {cantidad2} y con la cantidad de juegetes de payaso: {cantidad1} su peso seria de: {peso} kg")
