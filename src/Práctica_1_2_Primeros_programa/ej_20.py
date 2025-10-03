"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, 
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con 
este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión."""

active = True
while active:
    try:
        pref = "+34"
        num = "913724710"
        ext = "56"
        
        #1
        a = input("Ingresa el prefijo: ")
        if len(a) != len(pref):
            print("La extension es incorrecta (￣へ￣()")

        #2
        b = input("Ingresa el numero del telefono: ")
        if len(b) != len(num):
            print("Faltan numeros (￣へ￣()")

        #3
        c = input("Ingresa la extension")
        if len(c) != len(ext):
            print("Error, esa extencion no vale (￣へ￣()")
        else:
            print(f"{a}-{b}-{c}")
            active = False


    except ValueError:
        print("Carajo!! Solo se pude poner numero aqui (￣へ￣()")
