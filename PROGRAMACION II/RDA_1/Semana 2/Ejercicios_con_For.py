"""for i in range (1,4):
#     print("hola", i")"""

"""
for j in range (0,5+1):
    print("Tabla del",j)
    for k in range (1,5+1):
        print(j,"*",k,"=",j*k)"""
"""        
for j in range (0,2+1):
    print("Tabla del",j)
    for l in range (1,2+1):
        for k in range (1,2+1):
            print(j,"*",k,"*",l,"=",j*k*l)"""
            
            
"""for i in range [10,45,30]:
    print("Su cuadrado es ", i**2)"""
"""
for j in [10,45,30]:
    for k in [35,2,9]:
        print("Su suma es ", j+k)"""
"""
for j in [10,45,30]:
    print("El elemento del ciclo es ", j)
    for k in [35,2,9]:
        print(j,"*",k,"=",j*k)"""
"""
for i in range(0,10+1):
    resto=i%2
    if resto==0:
        print(resto, "Es numero es par")
    else:
        print(resto, "El numero es impar")"""
        
def contacto(**info):
    print("Datos de contacto")
    for clave, valor in info.items():
        print(clave, ":", valor)
"""
contacto(nombre="Edison", email="ajsuthercv@gmail.com")
print("\n")
contacto(nombre="Edison", email="ajsuthercv@gmail.com", telefono="0987654321")"""


#Programacion orientada a objetos
#es un paradigma de programacion que se basa en la creacion de objetos que contienen tanto datos como metodos para manipular esos datos.
#Los objetos son instancias de clases, que son plantillas que definen la estructura y el comportamiento de los objetos.

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
