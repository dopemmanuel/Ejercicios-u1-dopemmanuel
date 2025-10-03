"""Realiza un programa en Python que solicite un nombre y una edad.

Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir"."""


name = input("Ingrese su nombre → ")
age = int(input("Ingrese su edad → "))

while age < 0:
    print("ES IMPSIBLE QUE TENGAS ESA EDAD")
    age = int(input("Ingrese su edad → "))

if name == "":
    name = "Desconocido"

max_age = 125 - age
if age > 125:
    print(f"Parece que dios si tiene favoritos, eres longevo!!\nTe llamas {name} y tienes {age} años, ya has sobrepasado la edad maxima. ")
else:
    print(f"Te llamas {name} y tienes {age} años, te quedan aún {max_age} años por cumplir")