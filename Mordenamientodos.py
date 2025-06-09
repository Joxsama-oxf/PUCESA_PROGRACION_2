""""Una empresa desea analizar cuál método de ordenamiento le conviene más para ordenar listas pequeñas
    de productos según su precio. Para ello, te ha encargado realizar un comparador práctico entre 
    tres algoritmos clásicos de ordenamiento: Bubble Sort, Insertion Sort y Selection Sort."""

while True:
   
    try:
      print("\n<----------    ✨ MENÚ ✨    ---------->")
      print("\n|<1>| Bubble Sort |<1>|")
      print("|<2>| Insertion Sort |<2>|")
      print("|<3>| Selection Sort |<3>|")
      print("|<4>| SALIDA |<4>|")

      opcion = int(input("\n|| Selecciona una opción del menú ||--> "))
    except ValueError:
      print("\nError: Por favor, ingrese un número válido.")
      continue
    
    Numeros=[2,6,9,3,1,4,0,7,8,5]
    if opcion == 1:
        def bubble_sort(lista):
            comparaciones = 0
            intercambios = 0
            n = len(lista)
            for i in range(n):
                for j in range(0, n-i-1):
                    comparaciones += 1
                    if lista[j] > lista[j+1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
                        intercambios += 1
            print(f"C: {comparaciones}")
            print(f"I.A: {intercambios}")

            return lista
        

        print("\nLista original:", Numeros)
        sorted_list = bubble_sort(Numeros.copy())
        print("Lista ordenada con Bubble Sort:", sorted_list)
    
    elif opcion == 2:
        def insertion_sort(lista):
            comparaciones = 0
            intercambios = 0
            for i in range(1, len(lista)):
                key = lista[i]
                j = i - 1
                while j >= 0 and key < lista[j]:
                    comparaciones += 1
                    lista[j + 1] = lista[j]
                    intercambios += 1
                    j -= 1
                lista[j + 1] = key
            print(f"C: {comparaciones}")
            print(f"I.A: {intercambios}")    
            return lista

        print("\nLista original:", Numeros)
        sorted_list = insertion_sort(Numeros.copy())
        print("Lista ordenada con Insertion Sort:", sorted_list)

    elif opcion == 3:
        def selection_sort(lista):
            comparaciones = 0
            intercambios = 0
            for i in range(len(lista)):
                this = i
                for j in range(i+1, len(lista)):
                    comparaciones += 1
                    if lista[j] < lista[this]:
                        this = j
                        
                lista[i], lista[this] = lista[this], lista[i]
                intercambios += 1 if this != i else 0
            print(f"C: {comparaciones}")
            print(f"I.A: {intercambios}")

            return lista

        print("\nLista original:", Numeros)
        sorted_list = selection_sort(Numeros.copy())
        print("Lista ordenada con Selection Sort:", sorted_list)

    elif opcion == 4:  
        print("Saliendo")
        break


"""Como funciona cada algoritmo desde tu punto de vista"""
# Bubble Sort: Este algoritmo compara elementos adyacentes y los intercambia si están en el orden incorrecto.
# Osea vamos comparando cada número con el que está al lado y si están al revés, los cambiamos. Hacemos
#  esto varias veces hasta que todo esté en su sitio. Es como ir empujando los más grandes hasta el final.

# Insertion Sort: Este algoritmo construye la lista ordenada de forma incremental. Para decirlo de una forma
# mas simple, este es como cuando ordenas cartas en la mano, tomas una carta nueva
# y la vas metiendo en el hueco correcto entre las que ya tienes ordenadas.

# Selection Sort: Este algoritmo divide la lista en dos partes: una ordenada y otra desordenada.
# Encuentra el elemento más pequeño de la parte desordenada y lo intercambia con el
#  primer elemento de la parte desordenada. un ejemplo: aqui vamos a ir buscando el número más pequeño de
#  toda la lista. Cuando lo encontramos, lo ponemos al principio. Luego, buscamos el más pequeño
#  del resto de la lista y lo ponemos en la siguiente posición. Seguimos así hasta que toda la
#  lista esté ordenada. Es como ir "seleccionando" el más pequeño que falta y poniéndolo en su lugar.


"""¿Cual es el mejor algoritmo?"""
#En este caso  Insertion Sort parece ser el más eficiente al hacer las comparaciones, pero tambien
#Selection Sort fue el más eficiente al hacer los intercambios. siento una lista pequeña, no habria mucha
#diferencia en lo que son los tres algoritmos

""""¿En qué situaciones usarías cada uno en la vida real o en software?"""
#Bubble short: Para propositos educativos o tambien par listas pequeñas
#Insertion Sort: Para listas pequeñas o tambien para cuando los datos ya están casi ordenados
#Selection Sort: para listas pequeñs o tengamos memoria limitada.
#  Cuando los intercambios son costosos ya que selection sort realiza la mínima cantidad
# de intercambios posible (O(n)), lo cual puede ser ventajoso si la operación de intercambio es muy
# costosa en un sistema particular