""" Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula."""

fraseAl = input("Introduce una frase o lo que sea...otra vez: ")
vocal = input("Introduce una bocal: ").lower()

if vocal in "aeiou":
    Modfrase = fraseAl.replace(vocal, vocal.upper())

    print(Modfrase)
