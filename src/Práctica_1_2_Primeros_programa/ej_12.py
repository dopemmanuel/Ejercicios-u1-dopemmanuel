"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal 
y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""

peso = float(input("Ingrese su peso: "))
estat = float(input("Ingrese su estatura: "))

if peso < 0:
    print("El peso no puede ser menor que 0") #el bucle no es necesario por el caso que aplica el enunciado, pero como sea lo agregue.

elif estat <= 0:
    print(f"la estatura no puede ser {estat}")

else:
    IMC = peso / (estat ** 2)
    print(f"Tu índice de masa corporal es {round(IMC,2)}, es el índice de masa corporal calculado redondeado con dos decimales.")
