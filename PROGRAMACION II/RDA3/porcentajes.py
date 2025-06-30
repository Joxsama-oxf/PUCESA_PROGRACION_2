#Como sacar el porcentaje de un numero
def porcentaje(parcial, total):
    if total == 0:
        return 0
    return (parcial / total) * 100


# Ejemplo de uso
#.2f

parcial = 30
total = 100
resultado = porcentaje(parcial, total)
print(f"El {parcial} es el {resultado:.2f}%")