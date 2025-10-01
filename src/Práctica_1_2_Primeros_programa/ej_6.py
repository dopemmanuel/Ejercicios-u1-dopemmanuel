"""Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""


Porciento = 10
ImporteFinal = int(input("Ingresa el importe final del artiuclo: "))


IVA = ImporteFinal * (1 + Porciento / 100)

IVA_pagado = ImporteFinal - IVA

print(f"El importe final es de {IVA_pagado}€")
