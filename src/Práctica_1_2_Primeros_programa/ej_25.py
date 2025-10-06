"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter."""


date = input("Introduce tu fecha de nacimiento: ").split("/")

if len(date) == 3:
    dia = date[0]
    mes = date[1]
    year = date[2]
else:
    print("Ese formato es incorrecto")


if len(dia) == 2 or 1 and len(mes) == 2 or 1 and len(year) == 4:

    dia = int(dia)
    mes = int(mes)
    year = int(year)

    if 1 <= dia <= 31 and 1 <= mes <= 12:
        print("Fecha válida")
        print(f"Nacistes el {dia}/{mes}/{year}")
    else:
        print("Día o mes fuera de rango")
else:
    print("Formato de día, mes o año incorrecto")
