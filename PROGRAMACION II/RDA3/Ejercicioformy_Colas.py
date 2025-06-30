class PacientesdeHospital:
    def __init__(self): # Lista vacía donde almacenaremos (prioridad, nombre)
       
        self.items = []
    
    def encolar(self, paciente, prioridad):# Agregar paciente como tupla (prioridad, nombre)

        self.items.append((prioridad, paciente))
        # Mostramos mensaje indicando qué elemento fue ingresado y su prioridad
        print(f"Ingresó: {paciente} con prioridad {prioridad}")

    def desencolar(self): # Atender paciente según prioridad
        if not self.esta_vacia():

            self.items.sort(key=lambda x: x[0])
            # Extraemos el primer elemento (mayor prioridad)
            atendido = self.items.pop(0)
            # Mostramos qué elemento fue atendido y su prioridad
            print(f"\nSe atendió: {atendido[1]} (Prioridad {atendido[0]})")
            print(f"Pacientes en espera: {self.tamaño()}")
            # Retornamos el elemento atendido por si se necesita usar
            return atendido 
        else:
            print("No hay clientes para atender.")
            return None
        
    def esta_vacia(self): # Verificar si hay pacientes
        return len(self.items) == 0

    def tamaño(self):# Retornar cantidad de pacientes en espera
        return len(self.items)

pacientes =  PacientesdeHospital()  
# Mostrar lista ordenada de pacientes pendientes   

pacientes.encolar("Pepito", 1)
pacientes.encolar("Juanito", 3)
pacientes.encolar("Maria", 2)
pacientes.encolar("Luis", 2)
pacientes.encolar("Ana", 1)
pacientes.encolar("Pedro", 3)
pacientes.encolar("Carla", 1)
pacientes.encolar("Sofia", 2)

"""pacientes.encolar("Pepito", 1)
pacientes.encolar("Juanito", 3)
pacientes.encolar("Maria", 2)
pacientes.encolar("Luis", 2)
pacientes.encolar("Ana", 1)
pacientes.encolar("Pedro", 3)
pacientes.encolar("Carla", 1)
pacientes.encolar("Sofia", 2)"""

while not pacientes.esta_vacia():
    pacientes.desencolar()