





clientes = [
    ("Carlos", 100.0),
    ("Ana", 50.5),
    ("Beatriz", 200.75),
    ("David", 25.0),
    ("Elena", 150.20),
    ("Fernando", 75.80),
    ("Gabriela", 300.0),
    ("Hugo", 120.50),
    ("Isabel", 90.15),
    ("Javier", 180.60)
]

print("Inventario original:")
for producto in clientes:
    print(producto)


def insertion_sort_por_nombre(lista):
    # Ordenamos los productos según su nombre (posición 0 de la tupla)
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0].lower() > actual[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def selection_sort_por_precio(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j][1] < lista[min_idx][1]:  # Comparamos por precio (índice 1)
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def busqueda_binaria_nombre(lista_ordenada, objetivo):
    inicio = 0
    fin = len(lista_ordenada) - 1
    comparaciones = 0

    while inicio <= fin:
        comparaciones += 1
        medio = (inicio + fin) // 2
        nombre = lista_ordenada[medio][0].lower()

        if nombre == objetivo.lower():
            return medio, comparaciones
        elif objetivo.lower() < nombre:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1, comparaciones