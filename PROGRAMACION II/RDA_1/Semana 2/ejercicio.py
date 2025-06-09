
class Persona:
    def __init__(self, nombre, edad, ocupacion): #self no es un parametro
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        
        
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupacion: {self.ocupacion}"
    
def mostrar_menu():
    print("Gestion de personas")
    print("1. agregar persona")
    print("2. mostrar personas")
    print("3. buscar persona")
    print("4. salir")
    
personas = []

while True:
    mostrar_menu()
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        ocupacion = input("Ingrese la ocupacion: ")
        nueva_persona = Persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(nombre, " Ha sido agregada exitosamente.")
        
    elif opcion == "2":
        if len(personas) > 0:
            print("Lista de personas:")
            for persona in personas:
                print(persona.descripcion())
        else:
            print("No hay personas registradas.")
            
                
    elif opcion == "3":
            nombre_buscar = input("Ingrese el nombre de la persona a buscar: ")
            encontrado = False
            for persona in personas:
                if persona.nombre.lower() == nombre_buscar.lower():
                    print("Persona encontrada:")
                    print(persona.descripcion())
                    encontrado = True
                    break
            if not encontrado:
                print("Persona no encontrada.")
            
    elif opcion == "4":
        print("Saliendo del programa.")
        break
        
    else:
        print("Opcion invalida. Intente nuevamente.")
        