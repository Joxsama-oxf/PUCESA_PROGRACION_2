"""Estudiante: Alejandro SUtherland
   Fecha: 16/06/2025
   Clase: Programacion II
"""


#Pila original
Pila = []
print("\nHistorial de pila", Pila)

# Agregar elementos a la pila
Pila.append("Hacer la trea")
Pila.append("Estudiar para el examen")
Pila.append("Llamar a un amigo")
Pila.append("Comprar comida")
Pila.append("Limpiar la casa") 
Pila.append("Hacer ejercicio")
Pila.append("Leer un libro")
Pila.append("Ver una pelicula")
Pila.append("Escuchar musica")
Pila.append("Jugar videojuegos")
print("\nHistorial de pila", Pila)

print("\nUltimo elemento de la pila:", Pila[-1])

Eliminacion = Pila.pop()
print("\nElemento que fue eliminado:", Eliminacion)
print("\nHistorial de pila", Pila)

#Ver si el historial de esta pila esta vacio
if len(Pila) == 0:
    print("\nEl historial de la pila esta vacio")
else:
    print("\nEl historial de la pila no esta vacio")
    print("\nHistorial de pila", Pila,"\n\n\n")


class ColaClientes:
    def __init__(self): # Lista vacía donde almacenaremos (prioridad, nombre)
       
        self.items = []
    
    def Cliente_en_espera(self, Cliente, prioridad):# Agregar Cliente como tupla (prioridad, nombre)

        self.items.append((prioridad, Cliente))
        # Mostramos mensaje indicando qué elemento fue ingresado y su prioridad
        print(f"Ingresó: {Cliente} con prioridad {prioridad}")

    def Atentido(self): # Atender Cliente según prioridad
        if not self.esta_vacia():

            self.items.sort(key=lambda x: x[0])
            # Extraemos el primer elemento (mayor prioridad)
            atendido = self.items.pop(0)
            # Mostramos qué elemento fue atendido y su prioridad
            print(f"\nSe atendió: {atendido[1]} (Prioridad {atendido[0]})")
            print(f"Clientes en espera: {self.tamaño()}")
            # Retornamos el elemento atendido por si se necesita usar
            return atendido 
        else:
            print("No hay clientes para atender.")
            return None
        
    def esta_vacia(self): # Verificar si hay Clientes
        return len(self.items) == 0

    def tamaño(self):# Retornar cantidad de Clientes en espera
        return len(self.items)

Clientes =  ColaClientes()  
# Mostrar lista ordenada de Clientes pendientes   

Clientes.Cliente_en_espera("Pepito", 1)
Clientes.Cliente_en_espera("Juanito", 3)
Clientes.Cliente_en_espera("Maria", 4)
Clientes.Cliente_en_espera("Luis", 2)
Clientes.Cliente_en_espera("Ana", 1)
Clientes.Cliente_en_espera("Pedro", 3)
Clientes.Cliente_en_espera("Carla", 4)
Clientes.Cliente_en_espera("Sofia", 2)

while not Clientes.esta_vacia():
    Clientes.Atentido()


"""Reflexión final

Explica en tus propias palabras: ¿Qué diferencias observas entre el funcionamiento de una PILA y
una COLA CON PRIORIDAD?"""

# La principal diferencia es que la pila es algo mas simple ya que solo tratamos en un solo sentido
# (LIFO - Last In First Out), mientras que la cola con prioridad nos permite manejar elementos por lo cual
# se hace mas complicado ya que son varios elementos y tenemos que tener en cuenta la prioridad de cada uno.

# En una pila, el último elemento agregado es el primero en ser eliminado.

# En una cola con prioridad,los elementos se eliminan según su prioridad,
# independientemente de cuándo fueron agregados.

#Es lo que mas puedo decir de esto