from collections import deque
import time
import random
estanormal=[]
estaprioridad=[]
cola_normal = deque()
########################################################################################################################|
def suma_normal():
    return sum(estanormal)
def suma_prioridad():
    return sum(estaprioridad)
########################################################################################################################|
class Clientes:
    def __init__(self,nombre):
        self.nombre = nombre
        self.items = []

class ClientesPrioridad(Clientes):
    def __init__(self,nombre,prioridad):
        super().__init__(nombre)
        self.prioridad = prioridad

    def encolar(self, nombre, prioridad):
        self.items.append((prioridad, nombre))
        print(f"Ingresó: {nombre} con prioridad {prioridad}")

    def desencolar(self):
        if not self.vacia():
            self.items.sort(key=lambda x: x[0]) # Ordena para que la prioridad más baja esté primero
            atendido = self.items.pop(0)
            print(f"\nSe atendió: {atendido[1]} (Prioridad {atendido[0]})")
            print(f"Clientes en fila: {self.tamaño()}")
            return atendido
        else:
            print("No hay clientes para atender.")
            return None

    def vacia(self):
        return len(self.items) == 0

    def tamaño(self):
        return len(self.items)

#######################################################################################################################
def generar_ticket(nombre, tipo, viaje):
        print(f"Generando ticket para {nombre} ({tipo}) del viaje {viaje}")
        time.sleep(0.5)
        print(f"Ticket generado: {nombre} - {tipo} - Viaje {viaje}")
        time.sleep(0.5)


CAPACIDAD_VAGON = 4
# Definimos una función para cargar el vagón con los clientes de ambas colas
def cargar_vagon(cola_prioridad: ClientesPrioridad, cola_normal: deque):
    pasajeros = []

    while len(pasajeros) < CAPACIDAD_VAGON:
        if not cola_prioridad.vacia(): # Usamos el objeto ClientesPrioridad
            time.sleep(random.uniform(0.5, 1.0))
            prioridad, nombre_cliente = cola_prioridad.desencolar()
            pasajeros.append(f"{nombre_cliente} (Prioridad: {prioridad})")
            print(f"Subió al vagón: {nombre_cliente} (Prioridad: {prioridad})")
            if prioridad ==True:
                estaprioridad.append(1)
            else:
                estanormal.append(1)
            generar_ticket(nombre_cliente, "Prioridad", len(pasajeros) + 1)

        elif len(cola_normal) > 0: # Usamos la deque para la cola normal
            time.sleep(random.uniform(0.5, 1.0))
            nombre_cliente = cola_normal.popleft()
            pasajeros.append(nombre_cliente)
            print(f"Subió al vagón: {nombre_cliente} (Regular)")
        else:
            print("No hay más clientes en ninguna cola para cargar el vagón.")
            break
    print(f"\nVagón cargado con: {pasajeros}")
    return pasajeros
####
DURACION_VIAJE = 1
####
def simular_viaje(pasajeros, numero_viaje):
    print(f"\n Viaje #{numero_viaje} con: {pasajeros}")
    for t in range(DURACION_VIAJE):
        print(f"   Turno {t+1}/{DURACION_VIAJE}")
        time.sleep(1)
    print("¡Viaje finalizado!")

##########################################################################################################################
def iniciar_simulacion(turnos_totales, cola_prioridad_instance, cola_normal):
    viaje_num = 1

    for turno in range(turnos_totales):
        print(f"--- Turno {turno+1}/{turnos_totales} ---")

        cantidad = random.randint(1, 3)
        for _ in range(cantidad):
            nombre = random.choice(["Ana", "Luis", "Carlos", "Sofía", "Mateo", "Valentina"])
            es_prioridad = random.random() < 0.3

            if es_prioridad: #cliente con prioridad
                # Asignamos una prioridad aleatoria (ej. 1 a 3, 1 siendo la más alta)
                prioridad = random.randint(1, 3)
                cola_prioridad_instance.encolar(nombre, prioridad)
            else: # Si es cliente normal
                cola_normal.append(nombre)
                print(f"Ingresó: {nombre} (Regular)")

        # La condición para iniciar un viaje debe incluir el tamaño de la cola de prioridad gestionada
        # por ClientesPrioridad, así que usamos cola_prioridad_instance.tamaño()
        if cola_prioridad_instance.tamaño() + len(cola_normal) >= CAPACIDAD_VAGON:
            pasajeros = cargar_vagon(cola_prioridad_instance, cola_normal)
            simular_viaje(pasajeros, viaje_num)
            viaje_num += 1
        else:
            print("Aún no hay suficientes personas para el viaje.")
        print(f"Clientes en espera (Prioridad): {cola_prioridad_instance.tamaño()}")
        print(f"Clientes en espera (Normal): {len(cola_normal)}")


####################################################################################################################################

Clientesa = ClientesPrioridad("Cola de prioridad", 0)
# Clientesb es un ejemplo de Clientes, pero la cola_normal global (deque) ya está siendo usada directamente
# Clientesb = Clientes("Cola normal")

# Iniciamos la simulación pasando las instancias correctas de las colas
iniciar_simulacion(turnos_totales=10, cola_prioridad_instance=Clientesa, cola_normal=cola_normal)

print("\n--- Finalizando procesamiento de colas restantes ---")
while not Clientesa.vacia():
    Clientesa.desencolar()

while len(cola_normal) > 0:
    print(f"\nSe atendió cliente normal, restante: {cola_normal.popleft()}")
#############################################################################################################
estadisticas_finales= (suma_normal(), suma_prioridad())
print("\nclientes atendidos en la cola normal", estadisticas_finales [0],  
      "\nclientes atendidos en la cola de prioridad", estadisticas_finales [1])#porfin se sumo njd
#############################################################################################################
print("\n--- Simulación finalizada ---")