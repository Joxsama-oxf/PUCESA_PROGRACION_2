import random
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
from IPython.display import clear_output
import time as t
import bisect

lista = random.sample(range(0, 20), 15)

#mostrar la lista original
print("Lista original:", lista)

def bubble_sort_viz(lista, mostrar_pasos=False, pausa=0.3):

    comparaciones = 0
    intercambios = 0
    n = len(lista)
    pasos = []

    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                intercambios += 1

                pasos.append(lista.copy())

    return lista, comparaciones, intercambios, pasos


#  Función para animar Bubble Sort paso a paso
def animar_bubble_sort(pasos):
    for estado in pasos:
        clear_output(wait=True)

        plt.bar(range(len(estado)), estado, color='skyblue')

#título y etiquetas a la gráfica
        plt.title("Animación Bubble Sort")
        plt.xlabel("Índice")  # Eje X representa las posiciones de la lista
        plt.ylabel("Valor")   # Eje Y representa el valor de cada elemento
        plt.pause(0.3)

    plt.show()


# 🧪 Creamos una lista pequeña de 10 elementos aleatorios entre 1 y 20 para que la animación sea clara
lista_demo = random.sample(range(0, 20), 15)

# Ejecutamos bubble_sort_viz con mostrar_pasos=True para capturar cada paso intermedio
_, _, _, pasos_animacion = bubble_sort_viz(lista_demo, mostrar_pasos=True)

# Llamamos a la función de animación con los pasos registrados
animar_bubble_sort(pasos_animacion)

#___________________________________________________________________________________________________


ordenada = sorted(lista)

print("Original con Sorted():", lista)
print("Ordenada con Sorted():", ordenada)

#____________________________________________________________________________________________________
def animar_comparacion_sorted_bubble_simulada(lista, pausa=0.2):

    
    lista_sorted_final = sorted(lista)
    pasos_sorted=[]
    lista_simulada = lista.copy()
    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            # Sustituimos el valor por el que estaría en la lista ordenada
            lista_simulada[i] = lista_sorted_final[i]
        # Guardamos el paso simulado
        pasos_sorted.append(lista_simulada.copy())

    # Definimos el número total de pasos que tendrá la animación (el mayor entre ambos procesos)
    total_pasos = len(pasos_sorted)

#_________________________________________________________________________________________________

    for k in range(total_pasos):
        clear_output(wait=True) 

        fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        if k < len(pasos_sorted):
            axs[1].bar(range(len(pasos_sorted[k])), pasos_sorted[k], color='lightgreen')
            axs[1].set_title(f"sorted() - Paso {k+1}")
            axs[1].set_ylim(0, max(lista) + 5)
        else:
            axs[1].bar(range(len(lista_sorted_final)), lista_sorted_final, color='lightgreen')
            axs[1].set_title("sorted() - Final")

   
        plt.tight_layout()

        plt.pause(pausa)

    plt.show()

animar_comparacion_sorted_bubble_simulada(lista_demo)
#_________________________________________________________________________________________________

nueva_nota = int(input("Ingrese la nueva nota: "))  # puedes cambiar o pedir por input
bisect.insort(lista, nueva_nota)
print("✅ Lista después de insertar la nueva nota:", lista)

nota_buscar = int(input("Ingrse la nota que deseas buscar: "))  # puedes cambiar o pedir por input
posicion = bisect.bisect_left(lista, nota_buscar)
if posicion < len(lista) and lista[posicion] == nota_buscar:

    print(f"🔍 La nota {nota_buscar} se encuentra en la posición {posicion}")
else:
    print(f"❌ La nota {nota_buscar} no está en la lista.")

#_________________________________________________________________________________________________
#Compara y explica cuál enfoque fue más claro y eficiente.
# El enfoque de Bubble Sort es más visual y permite ver el proceso de ordenamiento paso a paso,
# mientras que el enfoque de sorted() es más eficiente y directo para ordenar listas grandes.
