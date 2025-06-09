





clientes = [
    ("carlos", 100.0),
    ("ana", 50.5),
    ("beatriz", 200.75),
    ("david", 25.0),
    ("elena", 150.20),
    ("fernando", 75.80),
    ("gabriela", 300.0),
    ("hugo", 120.50),
    ("isabel", 90.15),
    ("javier", 180.60)
]

j=print("Inventario original:")
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


"""* ¿Por qué es necesario ordenar antes de realizar la búsqueda binaria?
---> Porque esta necesita estar ordenada para poder dividir la lista en mitades y buscar eficientemente.
* ¿Qué pasaría si usamos búsqueda binaria sin ordenar primero?
---> No va a funcionar, ya que esta asume que la lista está ordenada y
     no podrá encontrar el elemento correctamente.
* ¿Qué ventajas viste entre la búsqueda binaria y la búsqueda lineal?
---> La búsqueda binaria es mucho más eficiente en listas grandes porque reduce el número de comparaciones,
     mientras que la búsqueda lineal revisa cada elemento uno por uno y si es una lista grande este gastara
     mas recursos.
* ¿Cuál de los dos ordenamientos te pareció más intuitivo de implementar y por qué?
---> Personalmente, me gusto mas el Insertion Sort porque es parecido a ordenar manualmente
     elementos en una lista."""

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i].lower() == objetivo.lower():
            return i
    return -1