"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el 
código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte 
por un número de teléfono con 
este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

active = True
pref = "+00"
num = "000000000"
ext = "00"
while active:
    try:

        a = input("Ingresa el prefijo: ")
        if len(a) != len(pref[0:2]):
            print("La extension es incorrecta (￣へ￣()")
            a = input("Ingresa el prefijo correctamente: ")
        else:
            b = input("Ingresa el numero del telefono: ")
            if len(b) != len(num[0:8]):
                print("Numeros incorrectos(￣へ￣()")
                b = input("Ingresa el numero del telefono correctamente: ")

            c = input("Ingresa la extension: ")
            if len(c) != len(ext[0:1]):
                print("Error, esa extencion no vale (￣へ￣()")
                c = input("Ingresa la extension correctamente: ")

        print(f"{a}-{b}-{c}")
        active = False


    except ValueError:
        print("Carajo!! Solo se pude poner numero aqui (￣へ￣()")
"""
active = True

pref = "+00"
num = "000000000"
ext = "00"
while active:
    try:
        a = input("Ingresa el prefijo: ")
        if (len(a) != len(pref[0:2]) or not a.startswith('+')):
            print("La extension es incorrecta (￣へ￣()")
            a = input("Ingresa el prefijo correctamente: ")
        else:
            b = input("Ingresa el numero del telefono: ")
            if (len(b) != len(num[0:9]) or not b.isdigit()):
                print("Numeros incorrectos(￣へ￣()")
                b = input("Ingresa el numero del telefono correctamente: ")
            else:
                c = input("Ingresa la extension: ")
                if len(c) != len(ext[0:1]) or not c.isdigit():
                    print("Error, esa extencion no vale (￣へ￣()")
                    c = input("Ingresa la extension correctamente: ")
                else:
                    print(f"{a}-{b}-{c}")
                    active = False

    except ValueError:
        print("Error!! Los campos solo son para los numeros.")
# WIP