# Calcular la serie de Fibonacci hasta un número dado

numero = int(input("Hasta donde quieres qque llegen los numeros?: "))
a = 0
b = 1

Fibonacci = []

for _ in range(numero):
    Fibonacci.append(a)
    a, b = b, a + b

print("Serie de Fibonacci:", Fibonacci)
