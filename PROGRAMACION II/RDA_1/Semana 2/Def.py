"""def funcion (nombre):
    print("esto es un ejemplo de funcion", nombre)
funcion("Alejandro")"""

"""def area_triangulo(base, altura):
    calc=base*altura/2
    print(calc)
#posisional
area_triangulo (2,3)
area_triangulo (4,5)"""

"""print("Argumentos por defecto")
def welcome(nombre, lenguage="Python"):
    print("bienvenido a", lenguage, nombre + "!")
welcome("Edison")
welcome("Edison", "Java")"""

print("pasar un numero indeterminado de argumentos")
def menu (*platos):
    print("Hoy tenemos:", end="") #el end va a hacer que todo se imprima en una linea
    for plato in platos:
        print(plato, end=",")
menu("sopa", "ensalada", "pasta", "carne")

"""
print("Las funciones son objetos de primera clase")
#ojo ojo ojo ojo
#en python, las funciones son objetos de primera clase, lo que significa que pueden ser tratadas como cualquier otro objeto.
def saludo(nombre):
    print("Hola", nombre)
    return
bienvenida=saludo #asignamos la funcion saludo a la variable bienvenida
bienvenida("Edison")"""
"""
print("funciones recursivas")
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Despegue!")
    print("Fin de la cuenta regresiva", numero)
cuenta_regresiva(5)"""

#posicional = respeta el orden
#posicional = no respeta el orden

#funciones recursivas con retorno

class Persona:
    def __init__(self, nombre, edad): #self no es un parametro
        self.nombre = nombre
        self.edad = edad
        
    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
persona1 = Persona ("Edison", 30)
persona2 = Persona ("Alejandro", 25)

print(persona1.descripcion())
print(persona2.descripcion())

#el metodo __init__ se llama automaticamente cuando se crea una instancia de la clase.
#se utiliza para inicializar los atributos de la clase.