"""Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".

num1 = int(input("Ingrese el primer numero → "))
num2 = int(input("Ingrese el segundo numero → "))


while (num1 == num2):
    print("Los numeros no pueden ser iguales")
    num2 = int(input("Ingrese el segundo numero → "))

if num1 > num2:
    menor = num2
    cantidad = num1 - num2
else:
    menor = num1
    cantidad = num2 - num1

print(f"El numero menor es el {menor} y entre ellos esxisten {cantidad} numeros enteros.")
"""
# Calcular el área de un triángulo a partir de tres lados
error = {
    'a': "No se permiten cadenas de caracteres y no se puede dejar vacío",
    'b': "El resultado no forma un triángulo válido"
}

active = True

while active:
    try:
        num1 = input("Ingresa el primer número: ")
        if not num1.strip() or not num1.isdigit():
            print(f"Error: {error['a']}")
            continue
        num1 = int(num1)

        num2 = input("Ingresa el segundo número: ")
        if not num2.strip() or not num2.isdigit():
            print(f"Error: {error['a']}")
            continue
        num2 = int(num2)

        num3 = input("Ingresa el tercer número: ")
        if not num3.strip() or not num3.isdigit():
            print(f"Error: {error['a']}")
            continue
        num3 = int(num3)

        if num1 + num2 <= num3 or num2 + num3 <= num1 or num3 + num1 <= num2:
            print(f"Error: {error['b']}")
            continue

        # Calcular el área (fórmula de Herón)
        perimetro = (num1 + num2 + num3) / 2
        area = (perimetro * (perimetro - num1) * (perimetro - num2) * (perimetro - num3)) ** 0.5
        print(f"El área del triángulo es: {area:.2f}")
        active = False

    except Exception as _:  # pylint: disable=broad-except
        print("Error!! Excepción General.")
