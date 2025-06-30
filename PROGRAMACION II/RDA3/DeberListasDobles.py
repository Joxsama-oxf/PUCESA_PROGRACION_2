class HistorialNavegador:
    def __init__(self, dato):
        self.dato = dato            # Dato almacenado
        self.anterior = None        # Referencia al nodo anterior
        self.siguiente = None 

class ListaDobleEnlazada:
    def __init__(self):
        # La cabeza apunta al primer nodo de la lista. Al inicio está vacía.
        self.cabeza = None

    def insertar_inicio(self, dato):
        # Crea un nuevo nodo con el dato recibido
        nuevo = HistorialNavegador(dato)
        # El nuevo nodo apunta como siguiente al que era la cabeza
        nuevo.siguiente = self.cabeza
        # Si la lista no está vacía, el nodo que era cabeza apunta hacia atrás al nuevo nodo
        if self.cabeza is not None:
            self.cabeza.anterior = nuevo
        # Ahora la cabeza de la lista es el nuevo nodo
        self.cabeza = nuevo

    def recorrer_adelante(self):
        # Comienza desde la cabeza de la lista
        actual = self.cabeza
        # Recorre la lista mientras haya nodos
        while actual is not None:
            print(actual.dato, end=" <-> ")  # Imprime el dato del nodo
            actual = actual.siguiente        # Avanza al siguiente nodo
        print("None")  # Indica el final de la lista

    def recorrer_atras(self):
        # Comienza desde la cabeza de la lista
        actual = self.cabeza
        if actual is None:
            print("Lista vacía")
            return
        # Avanza hasta el último nodo de la lista
        while actual.siguiente is not None:
            actual = actual.siguiente
        # Desde el último nodo, recorre hacia atrás usando el puntero 'anterior'
        while actual is not None:
            print(actual.dato, end=" <-> ")  # Imprime el dato del nodo
            actual = actual.anterior         # Retrocede al nodo anterior
        print("None")  # Indica el inicio

lista = ListaDobleEnlazada()

# Insertar elementos
lista.insertar_inicio("animeav1.com")
lista.insertar_inicio("youtube.com")
lista.insertar_inicio("pucesa.edu.ec")

# Recorrer hacia adelante
print("Recorrido hacia adelante:")
lista.recorrer_adelante()

# Recorrer hacia atrás
print("Recorrido hacia atrás:")
lista.recorrer_atras()

lista.insertar_inicio("luppet.com")
