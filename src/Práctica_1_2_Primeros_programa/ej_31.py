# Mostrar todos los divisores de un número

valor = int(input("Ingresa el numero: "))

print(f"Divisores de {valor}:")
for i in range(1, valor + 1):
    if valor % i == 0:
        print(i)
