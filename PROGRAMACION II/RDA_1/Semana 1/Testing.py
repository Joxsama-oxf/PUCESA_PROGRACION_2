"""Num1 = 5
Num2 = 9

if Num1 > 3 and Num2 < 10:
    print("Hola mundo")
else:
    print("Adios mundo")
"""

efectivo = "si" #solo una es si por que solo podemos pagar de un metodo
transferencia = "no"
tarjetacredito = "no"

if efectivo == "si" or transferencia == "si" or tarjetacredito == "si":
    print("Puede comprar el coche")
else:
    print("No puede comprar el coche")