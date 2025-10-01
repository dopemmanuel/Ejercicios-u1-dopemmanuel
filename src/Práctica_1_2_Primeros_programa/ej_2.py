"""Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio."""


horas = int(input("Ingresa las horas que has trabajado: "))
coste = int(input("Ingrese el coste por horas: "))


multi = horas * coste
print(f"Horas de trabajo: {horas}\nCoste por hora: {coste}\nImporte total: {multi}")
