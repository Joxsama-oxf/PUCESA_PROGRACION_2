"""Estudiante: Alejandro SUtherland
   Fecha: 09/06/2025
   Clase: Programacion II
   Tema: Pilas (son como listas con con una estructura LIFO - Last In First Out)
"""


#Pila original
Pila = []
print("\nHistorial de pila", Pila)

# Agregar elementos a la pila
Pila.append("www.google.com")
Pila.append("www.python.org")
Pila.append("www.stackoverflow.com")
print("\nHistorial de pila", Pila)

#Ver el ultimo elemento de la pila sin eliminarlo
print("\nUltimo elemento de la pila:", Pila[-1])

# Eliminar el ultimo elemento de la pila
Eliminacion = Pila.pop()
print("\nElemento que fue eliminado:", Eliminacion)
print("\nHistorial de pila", Pila)

#Ver si el historial de esta pila esta vacio
if len(Pila) == 0:
    print("\nEl historial de la pila esta vacio")
else:
    print("\nEl historial de la pila no esta vacio")
    print("\nHistorial de pila", Pila,"\n")

"""Como mantener la lista original y la pila actualizada
   - Mantener una lista original y una pila actualizada es útil para conservar el historial de cambios.
   - Cada vez que se agrega un elemento a la pila, también se puede agregar a la lista original.
   - De esta manera, se puede acceder a todos los elementos anteriores sin perder información.
# Ejemplo de mantener una lista original y una pila actualizada
# Lista original
Lista_original = ["www.google.com", "www.python.org", "www.stackoverflow.com"]
# Pila actualizada
Pila_actualizada = []
"""

"SOLO AGREGO UN CAMBIO"