"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""


sin_IVA = float(input("Ingrese el importe sin IVA de su articulo: "))
con_iva = int(input("Ingrese el porciento de IVA al aplicar: "))


divi = sin_IVA * (con_iva / 100)
multi =  sin_IVA + divi

print(f"Su Importe es de {sin_IVA}€ \nEl tipo de IVA a aplicar es de {con_iva}% \nEl precio fina del articulo es de {multi}€") # pylint: disable=line-too-long
