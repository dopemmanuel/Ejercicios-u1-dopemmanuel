"""Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.

El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros"."""

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