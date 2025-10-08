"""El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan
 un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10


# Solicitar el inicial, incremento y el total:
inicial = int(input("¿En que numero quieres comenzar? → "))
incremento = int(input("¿Por cuánto quieres incrementa? → "))
total = int(input("¿Hasta cuánto lo quieres incrementar? → "))
serie = ""

# Validar que los tres valores sean mayores que cero:
while incremento <= 0 or total <= 0 or inicial <= 0:
    print("EL VALOR NO PUEDE SER MENOR O IGUAL A 0")
    inicial = int(input("¿En que numero quieres comenzar? →"))
    incremento = int(input("Ingresa el número que quieres incrementar → "))
    total = int(input("¿Hasta cuánto lo quieres incrementar? → "))

#Usamos un bucle FOR
for i in range(inicial, total + 1, incremento):
    if inicial == i:
        serie += str(i) + "-"
    elif total == i:
        serie = serie[:-2:]
        serie += "-" + str(i)
    else:
        serie += str(i) + ".."

if (total - inicial) % incremento != 0:
    serie = serie[:-2:]
    serie += "-" + str(total)


print(f"SERIE => {serie}")
"""
# Escribir un programa que determine si un número es primo

num1 = int(input("Ingresa el numero y te dire si es primo o no: "))
found = False
i = 2
if num1 <= 1:
    print("No es primo")
elif num1 == 2:
    print("Es primo")
else:
    while i < num1 and not found:
        if (num1 % i) == 0:
            found = True
        i += 1
    if found:
        print("No es primo")
    else:
        print("Es primo")
